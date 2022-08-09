from load import load
import uuid


def transform_data(kafka_data: dict):
    data = {}
    user_id, movie_id = kafka_data['key'].decode('utf-8').split(':')
    data['user_id'] = uuid.UUID(user_id)
    data['movie_id'] = uuid.UUID(movie_id)
    data['movie_timestamp'] = kafka_data['value'].decode('utf-8')
    data['created_at'] = kafka_data['timestamp']

    load(data)