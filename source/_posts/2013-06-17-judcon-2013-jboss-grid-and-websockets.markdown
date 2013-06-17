---
layout: post
title: "JUDCon 2013: JBoss Data Grid and WebSockets"
date: 2013-06-17 09:16
comments: true
categories: [JUDCon, JBoss, WebSockets, Grid]
---

Delivering Real Time Push at Scale
==================================

_(Keeping an eye on the [WWDC](https://developer.apple.com/wwdc/) 
announcements)_

It's good to see a Linux OS doing the presenting, though it 
looks like Ubuntu, not RHEL?  Oh I see, hah! it's just a virtual 
machine.

[Mark Addy](http://blog.c2b2.co.uk) started the presentation by 
covering why we need to look at websockets and data grid solutions 
in general.  After all, if what we have today must already work, 
why do anything different?  The good news is, we can improve quite 
a bit.  Existing mechanisms for delivering (or simulating) real time 
data updates between a server and browser with HTTP are inherently
limited.  HTTP is a request-reply protocol, which means it is 
a half-duplex connection, like using a walkie-talkie pair for
each connection open between the client and server.  Worse, only
the client can initiate the connection.  In our use case here,
the client is the browser.  Comet Cursor techniques, like polling
or even long-polling doesn't cut it for high concurrency or 
high frequency updates.  Streaming over HTTP 1.1 connections is
not (as) memory efficient.

Enter WebSockets
----------------

WebSockets are available in HTML5 compliant browsers, described
by [RFC 6455](https://www.rfc-editor.org/rfc/rfc6455.txt) and in
JEE7 described by [JSR 356](http://jcp.org/aboutJava/communityprocess/final/jsr356/index.html).
WebSockets provide a protocol upgrade path from traditional 
HTTP, support full duplex communication (bidirectional
and simultaneous), support path parameters (_can you say: 
RESTful WebSockets?_) and use only 2 bytes overhead per frame.

JBoss Data Grid
---------------

[JBoss Data
Grid](https://www.redhat.com/products/jbossenterprisemiddleware/data-grid/)
is essentially a caching framework which includes data replication
and (re) distribution functionality.  This means that the sum of the 
data included in a JBoss Data Grid cache is equivalent to the number
of elements in the cache multiplied by the number of nodes and divided
by the number of copies of the data between nodes.  Redundancy is 
automatic with even data distribution.

For applications, a great feature of Data Grid is that as a
developer, you need not remember which node received data to retrieve 
it back again later.  The data grid will note the location of each 
entry and automatically retrieve it from any other node as necessary
when requested by an application.  Another is the support for _Cache
Events_.  Listening to cache events allows and application to take
advice from the cache when elements are changed or written.  For
example, in a dashboard if the source data aggregate changes in 
response to a recurring map-reduce job, data could be made available
to dashboard listeners by issuing a push or pull request after
receiving an event notification that the data had changed in the cache.

Currently, JBoss Data Grid can only be used in an embedded mode, as
a java library in an application.  Soon multiple modes will be supported,
such as a client-server mode.  If you are using the new 8.0.0
[WildFly](http://wildfly.org) application server then you can use 
library mode with JBoss Data Grid right away.

Optimizing Events
-----------------

Since multiple copies of data can exist in a distributed cache,
multiple events occur whenever data is updated as copies are refreshed.
An application most likely does not want to receive the additional
events and almost surely does not want to propogate a data refresh to
a WebSocket client connection if the data has not actually changed from
the first event received.  To resolve this, JBoss application servers
including HornetQ can enable the _de-duplication_ feature on a JMS
Topic, resulting in an automatic purging of the duplicate cache
events as they are published to the topic.  

  WebSocket Clients ............   *
             /|\
              |   (WebSocket Protocol)
             \|/
  Application Message Driven Beans (@ServerEndpoint)
             /|\
              |   (JMS via Subscription)
              |
  HornetQ Topic Publisher
    /|\     /|\    /|\
     |       |      |   (Data Grid Cache Events)
     |       |      |
  JBoss Data Grid Layer
     |    |    |    |
    |X| .......... |X|  (Data Grid Nodes)


_(WWDC Update: New MacBook Air with Haswell and a new MacPro!)_
