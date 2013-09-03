---
layout: post
title: "Atlanta JBUG: JBoss A-MQ is the hotness"
date: 2013-08-30 14:30
comments: true
categories: [RedHat, A-MQ, JBoss, Open Source, Apache, Active MQ]
---

Just before Labor Day weekend, Hiram Chirino came down to our Atlanta JBoss Users Group.  We had a large local turnout interested to know more about JBoss AM-Q and the features coming from Apache Active MQ upstream.  An accomplished engineer, Hiram is employed by Red Hat but is also an Apache member and ActiveMQ PMC chair.  Between committing to Apache ActiveMQ, Camel, Karaf, ServiceMix, Felix and Aries, Hiram leads the development of the STOMP 1.1 specification.  All those things in mind, it was our pleasure at Shadow-Soft to continue our tradition of hosting the recurring Atlanta JBUG meetup with a presenter that knows what he is talking about.


Messaging Oriented Middleware
============================

JBoss AMQ is an example of Messaging oriented Middleware (or MoM), which essentially means that JBoss A-MQ offers messaging APIs and facilities to deliver messages between message producers and message consumers in a variety of ways.  Hiram began by describing components in messaging, such as producers, consumers, topics, queues, destinations and selectors.  Using nicely animated slides to visually represent message delivery, Hiram conveyed the principle concepts of messaging that represent the baseline of functionality achieved by A-MQ prior to providing additional best in class level features.


Features
========

One differentiating factor of A-MQ is that it works hard to make messaging a commodity between different implementation languages, physical architectures and runtime environments.  For example, A-MQ supports multiple messaging protocols (itself converting to and from OpenWire internally) appropriate to a variety of use cases.  As well, A-MQ can be deployed embedded in another application, to a Web application server, to a JEE server, standalone or within a highly available message broker cluster.  The deployment flexibility, interoperability and multi-protocol support of A-MQ make it an ideal solution for supporting Smart Grids of large numbers of embedded and mobile devices.


Even More Features
==================

However, differentiating features do not stop there.  Some of the best features of A-MQ come right out of the wish list of engineers implementing messaging driven solutions.  These include:

* Wildcard destinations (instead of having to implement non-interrupting listeners with their own logic to determine if a message is of interest or using overly generic destination names)

* Composite destinations (instead of having to implement multiple listeners with identical implementations)

* Exclusive consumers (instead of having to implement logic or physical architecture to affect the sticky nature of a message recipient)

* Message groups (instead of having to implement both logical and physical architecture to manage message load and exclusivity simultaneously)

In any deployment strategy, A-MQ operates as a message broker, offering logic and functionality to accept messages from a variety of protocols in a variety of technologies and apply the necessary steps to reliably store and/or transmit those messages to a suitable destination.  However, the architecture of an A-MQ deployment is not limited to single-point; brokers can be networked together for the benefit of high availability, firewall traversal, store & forward function, and a global messaging namespace.  Particularly in corporate networks messaging to or from satellite locations, the ability to traverse firewalls and create a bi-directional connection to a known source or destination is a powerful feature.


Demo Time
=========

As A-MQ absorbs features from Apache ActiveMQ, Hiram walked us through a major upcoming feature: LevelDB support.  Level DB, and replicated Level DB support, stands to increase the base level of stored message performance by more than 100% over Kaha DB - the current default message store.

Finally, Hiram used Zookeeper, Active MQ and Level DB to demonstrate message replication, high availability broker configuration and both producer and consumer recovery scenarios when those processes experienced unexpected termination events.


Join Us
=======

Shadow-Soft is proud to continue hosting knowledge rich sessions in the Atlanta JBUG meetup.  We hope you will spend an evening with us for some knowledge sharing, personal networking and enlightening perspectives on Open Source developments in the JBoss universe.




