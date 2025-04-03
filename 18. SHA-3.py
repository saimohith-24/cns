import numpy as np
def initialize_state():
    """Initialize the SHA-3 state matrix with 1600 bits (5x5 lanes of 64 bits)."""
    return np.zeros((5, 5), dtype=np.uint64)  # 5x5 lanes, each 64 bits
def inject_message_block(state, block_size=1024):
    """Inject a message block ensuring at least one nonzero bit per lane in 1024-bit portion."""
    lanes_to_fill = block_size // 64  # Number of lanes covered by the message block
    for i in range(lanes_to_fill):
        x, y = divmod(i, 5)  # Assign lane positions in a 5x5 matrix
        state[x, y] = np.random.randint(1, 2**64, dtype=np.uint64)  # Ensure nonzero bits
    return state
def count_empty_lanes(state):
    """Count the lanes in the capacity portion that are still zero."""
    return np.sum(state == 0)  # Count lanes still at zero
def track_zero_lanes():
    """Track iterations needed until all capacity lanes have at least one nonzero bit."""
    state = initialize_state()
    rounds = 0
    while count_empty_lanes(state) > 9:  # 1600 - 1024 = 576 bits (9 lanes capacity)
        state = inject_message_block(state)
        rounds += 1
    return rounds
# Run the tracking simulation
rounds_needed = track_zero_lanes()
print(f"All capacity lanes have at least one nonzero bit after {rounds_needed} message block injections.")
