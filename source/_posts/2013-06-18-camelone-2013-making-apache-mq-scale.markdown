---
layout: post
title: "CamelOne 2013: Making Apache MQ Scale"
date: 2013-06-18 08:43
comments: true
categories: [Camel, CamelOne, ApacheMQ, Fuse]
---

[Hiram Chirino](http://hiramchirino.com/blog) is one of the authors of
Apache MQ, so this should be good.  

Apache MQ is designed for Machine to Machine, push-style messaging and
enables vertical scaling through high performance as well as 
horizontal scaling through clustering and partitioning.  Hiram gave
a number of scaling tips for Apache MQ, which should mostly apply to
[JBoss Fuse](https://www.redhat.com/products/jbossenterprisemiddleware/fuse/)
since Apache MQ is embedded.

Vertical Scaling
----------------

To start, vertical scaling, or allowing a single Apache MQ broker to
serve more traffic than before, can be improved with a few parameters:

* Set the configuration for using a dedicated task runner to false.
* Set the destination policy setting for optimizing dispatch to true.
* Use the NIO transport on the broker
* Reduce the thread size on the JVM via the Xss option

If using version 5.6 of Apache MQ, then non-blocking callbacks for 
ACK-ing receipt of JMS messages are available which can improve 
performance by incurring fewer thread waits.  

If using version 5.8, a new backing store is available, called
[Level DB](https://github.com/fusesource/fuse-extra/tree/master/fusemq-leveldb)
instead of [Kaha DB](https://activemq.apache.org/kahadb.html) which
offers higher performance in nearly all cases.  

Horizontal Scaling
------------------

Scaling _out_ is usally a little more tricky than scaling _up_.  In
Apache MQ, there are two primary methods for scaling out 
horizontally in your messaging architecture:

1. Use client side partitioning by having multiple brokers, each 
   for a set of clients.
2. Link brokers together in a cluster configuration.

The second method is the out of box "easy button", but it is
important to note that it does NOT make Apache MQ _faster_.  Instead,
in some cases it is _slower_ because it may add a network hop
between brokers to reach a particular connected client path.

The first method is more difficult to configure and maintain as 
clients scale out, so it is best used where the messaging topology
matches with the broker partitioning scheme. This occurs when clients
are naturally separated by geography or business purpose and 
producers _know_ which client group should receive a particular
message and can select the broker accordingly.

High Availability
-----------------

Even with Horizontal Scaling practices, it is still possible to lose a
broker and, particularly when using partioning, the associated set of
clients.  This is where a High Availability configuration comes into 
play - to allow clients to continue receiving messages when their
primary broker fails.

HA configurations often use a failover URI type, written as
`failover://(address1,address2,...)` but high availability can also
be acheived by clustering at the database level (which is still a 
single point of failure, only now at the DB instead of the message 
broker).  Alternately shared filesystems can be used and, in the case
of Apache MQ 5.9, a replicated Level DB using Zookeeper for automatic
leader election.

The [Zookeeper](https://zookeeper.apache.org/) case is an interesting
one, as it is also the officially supported tool embedded within
[Fuse Fabric](http://fusesource.com/products/fuse-fabric/) as the 
service registry.  When a fabric URI is used, the client can dynamically
discover and resolve slave instances of brokers from the directory.

It is important to consider the system load when using Zookeeper, as
Zookeeper does not respond well in cases of CPU contention and this 
can impact leader election.  Keeping Zookeeper hosted separately from
the Apache MQ broker helps with this, and you need at least 3 Zookeeper
instances to achieve High Availability through Zookeeper, and at least
5 to have high reliability.

Demo Time
---------

Hiram made use of [Tmux](http://tmux.sourceforge.net/) to automatically
echo his commands across multiple terminals, live in front of the 
audience.  This speeds up the demo quite a bit, looks awesome, and 
lends credibility to him as a presenter for using a cool tool.

The demo went well, showing brokers going down and the clients 
recovering without losing messages.  

Closing Thoughts
----------------

A lot of features are new in the 5.9 version of Apache MQ, but won't
make it into RedHat JBoss Fuse until early next year.  
RedHat JBoss Fuse sees Apache MQ as upstream code and takes some time
to certify it for enterprise level support.

