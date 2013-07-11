---
layout: post
title: "JUDCon 2013: Resilient Enterprise Messaging with Fuse &amp; Red Hat Enterprise Linux"
date: 2013-07-11 14:12
comments: true
categories: [JUDCon, Fuse, A-MQ]
---

This was the last session I attended prior to the start of the Summit
keynotes.  Presented by the Scotts (Cranton and McCarty), the session
turned out to be the very-high-level companion to Hiram's 'Making Apache
Active MQ Scale' session.  Unfortunately, this session wasn't nearly as
deep as it could have been.

Presented from a laptop _covered_ in stickers (but at least it was running
RHEL!), the session focused on the high level feature capabilities of
[JBoss FUSE](https://www.jboss.org/products/fuse) and A-MQ.

[JBoss A-MQ](https://www.jboss.org/jbossamq) is the enterprise certified
and supported release of Apache Active MQ, with multiple protocol and
language support.  FUSE embeds Active MQ into Karaf using [FUSE Fabric](http://fusesource.com/products/fuse-fabric/).

Some of the added features or benefits are:

* The ability to use one backing store per broker, but with separation to
  avoid blocking at the I/O controller
* An operations managed cluster instead of product level clustering using
  the Red Hat Cluster Suite
* N+1 or N+2 architecture for highly available message brokers instead of
  2N or more (like active/passive) configurations.

The good news is that since everything is open source, we can dig into the
[code](http://github.com/jboss-fuse).
