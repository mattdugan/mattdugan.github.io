---
layout: post
title: "JUDCon 2013: Building HTML5 Applications"
date: 2013-06-25 15:20
comments: true
categories: [JUDCon, HTML5, JBoss, Forge, Errai]
---

[JBoss](http://www.jboss.org) has been doing a lot of work (and a lot of 
writing) about their quick starts to application development on the JBoss
stack.  This is a _good thing_ as..

1.  All the code is open source
2.  JBoss has a huge number of projects and it can be difficult to make
    sense of them all without good examples.

Pete Muir (who could walk into any high school undetected) is 
a superb presenter and is an active participant in the JBoss quickstart
projects.

There are nearly 100 [JBoss Quickstarts](https://www.jboss.org/jdf/quickstarts/get-started/)
to assist developers and architects alike with doing their own work or just
getting familiar with the suite of JBoss projects available for use.  Most, if
not all, are available from GitHub and can be initalized using a maven 
command or two.  Some quickstart projects are implemented more than once, with
variation between the implementation technology.  This is another great 
technique for learning just what difference does using 
[Angular JS](http://angularjs.org/) vs [JBoss Errai](https://www.jboss.org/errai) 
or [RichFaces JSF](https://www.jboss.org/richfaces) make for an application 
(for example).

TicketMonster
-------------

The focus of today's presentation (and others to follow) was the 
[Ticket Monster](https://www.jboss.org/jdf/examples/ticket-monster/tutorial/WhatIsTicketMonster/)
example application.  It made use of several technologies, including the
new JEE-6 specification for CDI to inject implementations of common application
functionality into the business classes, [JBoss DataGrid](https://www.redhat.com/products/jbossenterprisemiddleware/data-grid/)
as an application object cache and a choice of view layers.  The application
is written in such a way as to have a different UI for both desktop and 
mobile view clients while maintaining a consistent service API on the JBoss
application server.  

As a shortcut for developing management UI capability for the various domain
objects in Ticket Monster, [JBoss Forge](http://forge.jboss.org/) was used
to generate the administration pages as scaffolds on top of the entity objects
for the Admin function.  This is a feature that has been around in Ruby and
Python domains for quite some time, and it is very good to see the scaffold
development utility appear in the Java space.

[JBoss Errai](https://www.jboss.org/errai) is used to provide a live data
binding between the UI and the server side of the application, which, via
Errai, automatically upgrades the connection to a WebSockets interleaved
stream when supported by both the browser and server.  Using CDI and events,
the communication between the client and server is highly interactive.

Closing Thoughts
----------------

It is a point of personal satisfaction to see so much work being done to 
help developers learn and do in creative work, especially so since all of 
the materials produced for the tutorials (and the application server itself)
is open source and available to all.  Kudos to the JBoss team and RedHat for 
not looking for a "line" between what is open and what is closed, but for
being all open, all the time.

