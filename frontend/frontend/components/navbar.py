import reflex as rx

def navbar() -> rx.Component:
    return rx.hstack(
        rx.text(
            "Neural network"
        )
    )