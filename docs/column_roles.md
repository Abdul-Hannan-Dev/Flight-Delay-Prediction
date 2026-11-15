Column	Role	Reason
MONTH	feature	Known in advance, and captures seasonal effects.
DAY_OF_WEEK	feature	Known in advance, with Monday = 1 (verified on your data).
FL_DATE	feature source	Used for derived features and as the key for time-based splits.
OP_UNIQUE_CARRIER	feature	The airline is known in advance.
TAIL_NUM	drop (v1)	Airlines swap aircraft late, users won’t know it, and thousands of IDs invite memorizing.
OP_CARRIER_FL_NUM	drop (v1)	An ID, not a quantity. It might be a key for history lookups in v2.
ORIGIN	feature	The route is published in advance.
DEST	feature	Same.
CRS_DEP_TIME	feature	Scheduled time. We extract the hour with // 100.
DEP_DELAY	leak	Exists only after the plane leaves the gate.
DEP_DEL15	leak	A yes/no version of DEP_DELAY.
TAXI_OUT	leak	Measured after pushback.
TAXI_IN	leak	Measured after landing.
CRS_ARR_TIME	feature	Scheduled arrival, known in advance.
ARR_DELAY	target	Regression target, and the source of our label.
ARR_DEL15	leak	BTS’s copy of the answer. We only use it to sanity-check our label.
CANCELLED	filter	Cancelled flights have no arrival, so they’re removed from training.
DIVERTED	filter	Same.
CRS_ELAPSED_TIME	feature	Scheduled trip length.
ACTUAL_ELAPSED_TIME	leak	Real trip length, known only after landing.
DISTANCE	feature	Fixed by the route.
five cause columns	leak	Filled only for late flights, so having a value reveals the label.