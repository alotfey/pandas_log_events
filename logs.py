import pandas as pd

expected_interval = 2 / 60  # 2 seconds converted to minutes

logs = [
    ('2023-06-01 10:00:00', 'Event 1'),
    ('2023-06-01 10:15:00', 'Event 2'),
    ('2023-06-01 10:30:00', 'Event 3'),
]
df = pd.DataFrame(logs, columns=['datetime', 'event_name'])
df['datetime'] = pd.to_datetime(df['datetime'])
df['duration'] = df['datetime'].diff()
df['duration_seconds'] = df['duration'].dt.total_seconds()
df['duration_minutes'] = df['duration'].dt.total_seconds().div(60)

df['delay'] = df['duration_minutes'].apply(lambda x: x - expected_interval if x > expected_interval else 0)

total_idle_time = df['delay'].sum()
total_idle_time_seconds = total_idle_time * 60

