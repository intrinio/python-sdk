

[//]: # (CLASS:AccountWebsocketStatus)

[//]: # (KIND:object)

### AccountWebsocketStatus

#### Properties

[//]: # (START_DEFINITION)

Name | Type | Description
------------ | ------------- | -------------
**feed** | str | The feed name for the connection. &nbsp;
**feed_connection_number** | int | The connection number for this account within a feed. &nbsp;
**ip** | str | The IP address detected for the client connection. &nbsp;
**connected_on** | datetime | The UTC time this client connection connected to the server. &nbsp;
**status_updated_on** | datetime | The UTC time the server updated this client connection status data. &nbsp;
**is_delayed** | bool | Whether this connection is delayed an extra 15 minutes from the source. Note that the Delayed SIP source is already delayed, so this value will be False for those connections. &nbsp;
**is_firehose** | bool | The client connection is in firehose mode (all channels subscribed). &nbsp;
**trade_subscriptions** | int | The count of channel subscriptions for trade events. &nbsp;
**quote_subscriptions** | int | The count of channel subscriptions for ask and bid events. &nbsp;
**refresh_subscriptions** | int | The count of channel subscriptions for refresh events (OPRA options feed only). &nbsp;
**unusual_activity_subscriptions** | int | The count of channel subscriptions for unusual activity events (OPRA options feed only). &nbsp;
**packets_per_second** | float | The packets per second sent since the last status update. &nbsp;
**total_packets_sent** | str | The total packets sent since the beginning of this connection.  A packet is a group of events sent as one message over the websocket. &nbsp;
**events_per_second** | float | The events per second sent since the last status update. &nbsp;
**total_events** | str | The total events sent to this connection&#39;s server-side queue since the beginning of this connection.  An event is an individual occurrence of a trade, quote, etc. &nbsp;
**total_sent_events** | str | The total events sent to the client inside packets. A packet is a group of events sent as one message over the websocket. &nbsp;
**total_drops** | str | The total number of events dropped from the connection&#39;s server-side queue.  Event drops happen when the connection&#39;s server-side queue is full. The server-side queue fills due to client-side connections not receiving packets fast enough, which can be caused by a slow network, or clients not decoupling processing of packets from the receipt of packets. &nbsp;
**queue_depth_percentage** | float | The percentage that the connection&#39;s server-side queue is full. 0-100. &nbsp;

[//]: # (END_DEFINITION)



