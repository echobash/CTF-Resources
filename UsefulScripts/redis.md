> Redis supports 5 data types. You need to know what type of value that a key maps to, as for each data type, the command to retrieve it is different.
Here are the commands to retrieve key value:

* if value is of type string -> GET <key>
* if value is of type hash -> HGETALL <key>
* if value is of type lists -> lrange <key> <start> <end>
* if value is of type sets -> smembers <key>
* if value is of type sorted sets -> ZRANGEBYSCORE <key> <min> <max>
* Use the TYPE command to check the type of value a key is mapping to:

> type key
