OBJECT_DB = {
    "ball": {
        "shape": "circle",
        "draw_fn": "drawBall",
        "physics": "bounce"
    },
    "bottle": {
        "shape": "cylinder",
        "draw_fn": "drawBottle",
        "physics": "rigid"
    },
    "chair": {
        "shape": "rectangular",
        "draw_fn": "drawChair",
        "physics": "static"
    },
    "box": {
        "shape": "cube",
        "draw_fn": "drawBox",
        "physics": "rigid"
    },
    "book": {
        "shape": "flat_rect",
        "draw_fn": "drawBook",
        "physics": "flexible"
    },
    "cup": {
        "shape": "cylinder",
        "draw_fn": "drawCup",
        "physics": "liquid_container"
    }
}
