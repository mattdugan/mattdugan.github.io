---
layout: post
title: "CamelOne 2013: Drools with Apache Camel.. Rules"
date: 2013-06-17 14:32
comments: true
categories: [Camel, CamelOne, Drools, BRMS]
---

Ah, the end of day Keynote, time to sit back and relax and
enjoy some light presentation that doesn't require any 
brain power at all.

... But it wasn't meant to be.  Mark Proctor was the presenter
and when they guy talking to you looks like he can juggle
a couple of Voltswagens, you had better listen.

jBPM, Drools, BRMS, what?
-------------------------

Coming from a background heavy in BPM, the confusion is 
natural and isn't exclusive to the decision maker, the 
implementer, or even the business user.  Each technology
has certain merits and this session helped to clarify
[Drools](https://www.jboss.org/drools/). Drools is not so 
much a "Business Rule" engine as it is a _Hybrid Reasoning
Engine_ supporting filters, logic, and chains.  Drools
includes features for CEP (Complex Event Processing),
Decision Tables for processing high numbers of rules and
_Time Windowing_ - a powerful feature allowing you to 
write logic for events that occur "over the last 5 minutes"
or other relative time periods.  

Next, we looked at BRMS, which packages Drools and jBPM 
together along with a rule repository to achieve a very
useful integration pattern.  Often, business users struggle
with expressing a complete process (as opposed to merely
a high-level process) in BPMN.  Eventually, the implementation
starts to look like code, graphical or not.  Rules, on
the other hand, *are* code but do not easily work upward
to describe an overall business process.  Putting the
two together is a peanut-butter-on-chocolate approach
designed to achieve common code patterns using Rule
logic while expressing the transitions between rule chains
and processes using BPMN.  This concept works surprisingly
well and I have to commend the RedHat BRMS team for 
thinking outside of the single-purpose tool package we see 
from other vendors.  

The upcoming release of BRMS embedding Drools 6 gains 
the ability of JBoss Truth Management to enable handling
of contraditions in the rule chain - for example a
discount rule of 10% and a temporary discount of 20% are
in conflict unless the contradiction can be managed to say
that the 20% rate is valid over a particular time window
and otherwise default to the 10% rule.  MultiCore processing
additions in Drools 6 should provide a significant speedup
in the next release of BRMS as well.

The Drools 6 UI gets a much needed refresh to fix some 
old nuances and adds resizable panels for getting work 
done within the browser viewport.  The new UI is brought
together with Errai _(see earlier post)_.  Rule storage
now has a GIT backend so rule authors can take advantage
of the GIT workflow for publishing rules.  Finally, work
has been performed to create a high availability scenario
for the rules engine and everything is built together
with maven.  Drools 6 introduces a new principal object
extension point, KIE, for "Knowledge is Everything".

Mark closed out the presentation with a brief note on
applying rules to situations you may not have thought of
as a convenient answer.  Watch Mark write Pong, implemented
in Drools.  

<https://www.youtube.com/watch?v=Omj4PR3v-nI>


