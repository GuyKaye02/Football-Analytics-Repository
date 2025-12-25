import pandas as pd
from tqdm.auto import tqdm
from statsbombpy import sb


def get_minutes_played4(df, match_id, player_id, match_durations):
    """
    Calculates minutes played for a player in a match using pre-calculated match durations.

    Args:
        df (DataFrame): DataFrame of events for the match.
        match_id (int): Match ID.
        player_id (int): Player ID.
        match_durations (DataFrame): DataFrame containing pre-calculated durations for each match and period.

    Returns:
        float: Total minutes played by the player in the match.
    """

    df['timestamp'] = pd.to_timedelta(df['timestamp'])

    player_info_df = df[(df['match_id'] == match_id) & (df['player_id'] == player_id)]
    if player_info_df.empty:
        return 0  # If player not found in the match, assume 0 minutes played

    team = player_info_df['team'].iloc[0]
    player_name = player_info_df['player'].iloc[0]

    try:
        lineup = df[(df['match_id'] == match_id) & (df['team'] == team) & (df['type'] == 'Starting XI')]['tactics'].values[0]
        starting_xi = [x['player']['name'] for x in lineup['lineup']]
        starter = player_name in starting_xi
    except IndexError:
        return 0

    durations = {
        period: match_durations[
            (match_durations['match_id'] == match_id) & (match_durations['period'] == period)
        ]['duration_minutes'].values[0] if not match_durations[
            (match_durations['match_id'] == match_id) & (match_durations['period'] == period)
        ]['duration_minutes'].empty else 0
        for period in range(1, 5)
    }

    min_played = 0

    if starter:
        min_played = sum(durations.values())
    
    else:
        entered = df[
            (df['match_id'] == match_id) &
            (df['team'] == team) &
            (df['type'] == 'Substitution') &
            (df['substitution_replacement'] == player_name)  # Changed from player to player_name
        ][['timestamp', 'period']]
        if not entered.empty:
            entered_period = entered['period'].values[0]
            entered_time = pd.Timedelta(entered['timestamp'].values[0]).total_seconds() / 60
            min_played = sum(durations[p] for p in range(entered_period+1, 5))  # Time in future periods
            min_played += (durations[entered_period] - entered_time) if entered_period in durations else 0  # Time in current period
    


    was_sub = df[
        (df['match_id'] == match_id) &
        (df['team'] == team) &
        (df['player_id'] == player_id) &
        (df['type'] == 'Substitution')
    ][['timestamp', 'period']]
    if not was_sub['timestamp'].empty:
        sub_period = was_sub['period'].values[0]
        sub_time = pd.Timedelta(was_sub['timestamp'].values[0]).total_seconds() / 60
        time_remaining_in_sub_period = durations[sub_period] - sub_time if sub_period in durations else 0
        min_played -= time_remaining_in_sub_period
        min_played -= sum(durations[p] for p in range(sub_period + 1, 5))

    was_excluded = df[
        (df['match_id'] == match_id) &
        (df['team'] == team) &
        (df['player_id'] == player_id) &
        (df.apply(lambda row: (
            row.get('bad_behaviour', {}).get('card', {}).get('name') in ['Red Card', 'Second Yellow'] or
            row.get('foul_committed', {}).get('card', {}).get('name') in ['Red Card', 'Second Yellow']
        ), axis=1))
    ][['timestamp', 'period']]
    if not was_excluded['timestamp'].empty:
        exclusion_period = was_excluded['period'].values[0]
        exclusion_time = was_excluded['timestamp'].values[0].total_seconds() / 60
        time_remaining_in_exclusion_period = durations[exclusion_period] - exclusion_time if exclusion_period in durations else 0
        min_played -= time_remaining_in_exclusion_period
        min_played -= sum(durations[p] for p in range(exclusion_period + 1, 5))

    return min_played

def get_all_minutes_by_match(match_ids, get_minutes_played_func):
    """Calculates total minutes played for all players across multiple matches.

    Args:
        match_ids (list): List of match IDs to process.
        get_minutes_played_func (function): Function to calculate minutes played for a player in a match.

    Returns:
        DataFrame: DataFrame with player IDs, names, total minutes, and teams.
    """

    all_player_minutes = []

    for match_id in tqdm(match_ids):
        events_df = sb.events(match_id)  # Load events for the current match
        match_durations = events_df.groupby(['match_id', 'period'])['timestamp'].max().reset_index()
        match_durations['duration_minutes'] = pd.to_timedelta(match_durations['timestamp']).dt.total_seconds() / 60
        all_players = events_df[['player_id', 'player', 'team']].drop_duplicates().dropna()

        for _, row in all_players.iterrows():
            player_id = row['player_id']
            player_name = row['player']
            team = row['team']

            min_played = get_minutes_played_func(events_df, match_id, player_id, match_durations)
            all_player_minutes.append([match_id, player_id, player_name, min_played, team])

    all_minutes_df = pd.DataFrame(all_player_minutes, columns=['match_id', 'player_id', 'player_name', 'minutes_played', 'team'])

    # Aggregate minutes played for each player across all matches
    final_df = all_minutes_df.groupby(['player_id', 'player_name', 'team'])['minutes_played'].sum().reset_index()
    final_df.rename(columns={'minutes_played': 'total_minutes'}, inplace=True)

    return final_df
