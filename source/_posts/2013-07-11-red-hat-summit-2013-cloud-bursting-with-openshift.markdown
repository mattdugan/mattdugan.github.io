---
layout: post
title: "Red Hat Summit 2013: Cloud Bursting with OpenShift"
date: 2013-07-11 16:57
comments: true
categories: [RedHat, Cloud, OpenShift]
---

It's 8PM, do you know where your true geeks are?  Well, the room was packed
for the Cloud Bursting with OpenShift birds of a feather session so the Red
Hat Summit 2013 in Boston might not be a bad guess.

[Grant Shipley](https://www.runcloudrun.com/) leads the session by
_skipping_ the "Intro to OpenShift" because 18 out of 20 people in the room
are already diving in.  Awesome.  Grant runs his _blog_ on
[OpenShift](http://www.openshift.com) making it one of the few that can
elastically scale in response to load.

OpenShift
---------

OpenShift is an ideal platform for deploying and hosting web applications
because of its architecture.
Supporting high deployment density is second nature and the ability to
scale out (or in) _automatically_ is just gravy.  When Grant's blog isn't
taking any traffic, his OpenShift platform consumption is effectively
zero.  But, under load, he could have hundreds of instances of the blog app
pumped up on the OpenShift hosting servers, without having to touch
anything or even worry about it.

The public OpenShift actually runs on
Amazon EWS, which was an intentional decision on the part of Red Hat at
design and development time.  They wanted to create a platform which was
inherently cloud scalable and deployable on local, hosted, and third party
architecture.  Since OpenShift first went into public beta 2 years ago (at
Red Hat Summit _2011_) there have been over a million applications created
on the platform.  Now, Openshift is available for paid, enterprise services
as well as self-hosted deployment.

For a demo, Grant showed the HA Proxy status page while performing a
web-base load test on his OpenShift application.  You could see as the
utilization reached a certain threshold that new instances were
automatically provisioned and taking traffic.  A minute after the requests
stopped coming in, or started coming in more slowly, extra instances were
de-provisioned.  This use case is great for applications which peak and
fall in terms of demand over time.  Even when the time scales are measured
in terms of minutes, the OpenShift architecture helps you ensure that your servers
are giving you their best, but only when necessary.

Pricing
-------

Hosting production applications on OpenShift is as easy as developing on
OpenShift, but there is some cost involved.  However, the pricing model
starts off very low because the architecture is capable of high vertical
density.  To run an application using 3 _Gears_ 24x7 (or 2,280 hours a
month) is free.  What's a Gear?  A SQL database is a Gear, an application
is a Gear, and any intermediary kind of platform is also a Gear.
Considering common 3-tier architecture, you could say "your first app is
free, but the next one might cost you".  What a great excuse to get started.

Uses
----

As was publicly announced at the Red Hat Summit, Accenture is standardizing
web deployment on OpenShift.  However, Accenture isn't the first.  Already
Web PaaS providers are popping up, such as GetUp Cloud in Brazil.  I'm sure
I'll be entering the fray quite soon myself with
[Shadow-Soft](http://www.shadow-soft.com).

Architecture
------------

Not all containers are created equal.  OpenShift does advertise a container
architecture, but it is important to note that "container", in this case,
is not a proper noun.  It does not refer to "Linux Containers".  Instead,
it is a classical (and clever) configuration of CPU Groups, SE Linux
policies, and permissions which come together to provide _containment_ to
individual user and application tenants on the OpenShift hosting platform.
When you install OpenShift yourself, you can use these techniques to say
"user 'x' has a minimum of 30% memory and CPU before scaling starts" and
other such logical scaling boundaries.

Community
---------

OpenShift is *very* active right now, primarily on IRC via the
`#OPENSHIFT_DEV` channel on FreeNode.  Generally, members of the
development team are always online somewhere in the world and a
conversation is flowing between users and developers.  Try getting that
with commercial proprietary software. :-)

Closing Thoughts
----------------

OpenShift is the most exciting thing Red Hat has going right now, in my
opinion.  I am eager to work with it on premise.  The advantages it
gives in deployment scalability for web applications (or, can you say, Web
_APIs_?) is a blast from the past of hand tuned high performance web
hosting services with all the benefits of modern application and user
separatation and on-demand (on HTTP request) elastic scaling.

Also, the _My app runs on OpenShift_ track jacket I picked up for deploying
on OpenShift live while at the Summit is sweeeeeeeeeeeeeeeet.

