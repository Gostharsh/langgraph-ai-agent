def get_successful_observations(observations):

    return [
        obs
        for obs in observations
        if obs.success
    ]