ENTITY_DB = {
    "man": {
        "type": "human",
        "skeleton": "biped",
        "draw_fn": "drawHuman",
        "attributes": ["adult", "male"]
    },
    "woman": {
        "type": "human",
        "skeleton": "biped",
        "draw_fn": "drawHuman",
        "attributes": ["adult", "female"]
    },
    "person": {
        "type": "human",
        "skeleton": "biped",
        "draw_fn": "drawHuman",
        "attributes": ["generic"]
    },
    "child": {
        "type": "human",
        "skeleton": "biped",
        "draw_fn": "drawHuman",
        "attributes": ["young", "short"]
    },
    "robot": {
        "type": "robot",
        "skeleton": "mechanical_biped",
        "draw_fn": "drawRobot",
        "attributes": ["metallic"]
    },
    "dog": {
        "type": "animal",
        "skeleton": "quadruped",
        "draw_fn": "drawDog",
        "attributes": ["pet"]
    }
}
