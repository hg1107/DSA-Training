import streamlit as st  # pyright: ignore[reportMissingImports]

# ----------------------------
# Queue implementation (fixed)
# ----------------------------
class Queue:
    def __init__(self, size):
        self.size = size
        self.queue = []

    def is_full(self):
        return len(self.queue) == self.size

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, item):
        if self.is_full():
            return False, "Queue is full. Cannot enqueue."
        self.queue.append(item)
        return True, f"Enqueued: {item}"

    def dequeue(self):
        if self.is_empty():
            return False, "Queue is empty. Cannot dequeue."
        item = self.queue.pop(0)
        return True, f"Dequeued: {item}"

    def peek_front(self):
        if self.is_empty():
            return False, "Queue is empty. No front item."
        return True, f"Front item: {self.queue[0]}"

    def delete_queue(self):
        self.queue = []
        return True, "Queue deleted."


# ----------------------------
# Streamlit app
# ----------------------------
st.set_page_config(page_title="FIFO Queue Visualizer", page_icon="🧮", layout="centered")

st.title("🧮 FIFO Queue Visualizer")
st.caption("A simple array-based Queue (FIFO) implementation with a live visual frontend.")

# Initialize queue in session state
if "queue_obj" not in st.session_state:
    st.session_state.queue_obj = None
if "log" not in st.session_state:
    st.session_state.log = []

with st.sidebar:
    st.header("⚙️ Setup")
    size = st.number_input("Queue capacity", min_value=1, max_value=50, value=5, step=1)
    if st.button("Create / Reset Queue", use_container_width=True):
        st.session_state.queue_obj = Queue(size)
        st.session_state.log = []
        st.success(f"Queue created with capacity {size}")

if st.session_state.queue_obj is None:
    st.info("👈 Create a queue from the sidebar to get started.")
    st.stop()

q = st.session_state.queue_obj

st.subheader("Operations")
col1, col2 = st.columns([2, 1])
with col1:
    item = st.text_input("Item to enqueue", key="item_input")
with col2:
    st.write("")
    st.write("")
    if st.button("➕ Enqueue", use_container_width=True):
        if item.strip() == "":
            st.warning("Enter a value first.")
        else:
            ok, msg = q.enqueue(item)
            st.session_state.log.insert(0, msg)

b1, b2, b3, b4 = st.columns(4)
with b1:
    if st.button("➖ Dequeue", use_container_width=True):
        ok, msg = q.dequeue()
        st.session_state.log.insert(0, msg)
with b2:
    if st.button("👀 Peek Front", use_container_width=True):
        ok, msg = q.peek_front()
        st.session_state.log.insert(0, msg)
with b3:
    if st.button("🗑️ Delete Queue", use_container_width=True):
        ok, msg = q.delete_queue()
        st.session_state.log.insert(0, msg)
with b4:
    if st.button("🔄 Clear Log", use_container_width=True):
        st.session_state.log = []

st.divider()

# Visual representation
st.subheader("Queue State")
status_col1, status_col2, status_col3 = st.columns(3)
status_col1.metric("Size", f"{len(q.queue)} / {q.size}")
status_col2.metric("Empty?", "Yes" if q.is_empty() else "No")
status_col3.metric("Full?", "Yes" if q.is_full() else "No")

if q.is_empty():
    st.write("The queue is empty.")
else:
    cells = " → ".join(f"**[{v}]**" for v in q.queue)
    st.markdown(f"**Front** → {cells} ← **Rear**")
    box_html = "".join(
        f"<span style='display:inline-block;padding:10px 16px;margin:4px;"
        f"border:2px solid #4CAF50;border-radius:8px;background:#f0fff0;"
        f"font-weight:bold;'>{v}</span>"
        for v in q.queue
    )
    st.markdown(box_html, unsafe_allow_html=True)

st.divider()
st.subheader("Activity Log")
if st.session_state.log:
    for entry in st.session_state.log:
        st.text(entry)
else:
    st.caption("No operations yet.")