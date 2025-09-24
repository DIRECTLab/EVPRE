AttributeError                            Traceback (most recent call last)
File ~/miniconda3/envs/test_evpre/lib/python3.10/site-packages/ipywidgets/widgets/widget.py:773, in Widget._handle_msg(self, msg)
    771         if 'buffer_paths' in data:
    772             _put_buffers(state, data['buffer_paths'], msg['buffers'])
--> 773         self.set_state(state)
    775 # Handle a state request.
    776 elif method == 'request_state':

File ~/miniconda3/envs/test_evpre/lib/python3.10/site-packages/ipywidgets/widgets/widget.py:650, in Widget.set_state(self, sync_data)
    645         self._send(msg, buffers=echo_buffers)
    647 # The order of these context managers is important. Properties must
    648 # be locked when the hold_trait_notification context manager is
    649 # released and notifications are fired.
--> 650 with self._lock_property(**sync_data), self.hold_trait_notifications():
    651     for name in sync_data:
    652         if name in self.keys:

File ~/miniconda3/envs/test_evpre/lib/python3.10/contextlib.py:142, in _GeneratorContextManager.__exit__(self, typ, value, traceback)
    140 if typ is None:
    141     try:
--> 142         next(self.gen)
    143     except StopIteration:
    144         return False
...
    103         self.graph, event_owner.location)
    104     marker.neares_node = ox.get_nearest_node(self.graph, marker.location)
    106     if self.compare_mode:

AttributeError: module 'osmnx' has no attribute 'get_nearest_node'