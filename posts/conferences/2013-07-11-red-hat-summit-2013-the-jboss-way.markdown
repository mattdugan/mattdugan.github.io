title: Red Hat Summit 2013: The JBoss Way
date: 2013-07-11 16:05
tags: JBoss, RedHat, Summit, AngularJS, EAP
category: Conferences
author: Matt Dugan
slug: rhsummit-2013-the-jboss-way
summary: Red Hat Summit 2013 talk summary on developing in "The JBoss Way", using JBoss tools, patterns, and technology.

Pete Muir was the presenter again, tailing off from his prior session on
_Building HTML5 Applications_.  This session should have some code examples
and more insights.

Diving into the code for the quickstarts, Pete makes a plug for
[AngularJS](http://www.angularjs.org/) and is clearly a big fan.  The
_difference_ with Angular JS is that it feels like using a tag library
language rather than applying text base templates for substitution.  The
negative point is that since AngularJS does not use `data-` attribute
prefixes, each `ng-` attribute gets the red underline because it isn't
following the HTML5 doctype.  Shame.

Still, being able to see the same or similar quick starts represented with
variations on the implementation choices is the next best thing to diving
into a framework and trying to make something useful yourself.

The [Quickstarts](https://www.jboss.org/jdf/quickstarts/get-started/)
source code is always available on [GitHub](https://github.com/jboss-jdf/
jboss-as-quickstart) and the individual pages for the quick start guides
have comments enabled which the authors tend to respond to.  This
communication is key since there are nearly 100 quick starts right now to
absorb and make sense of.

Code examples are presented using [JBoss Developer Studio](https://devstudio.jboss.com/download/6.x.html), the enterprise version of the
JBoss IDE.  The examples are executing on [JBoss EAP 6](http://www.redhat.com/products/jbossenterprisemiddleware/application-platform/), the
enterprise version of Wildfly (JBoss Application Server - Community Edition).

The workflow of making code changes or developing a project that you want
to deploy to your configured server from within the developer studio is
simple: just drag and drop the application module onto the server
configuration and it will deploy in the console.

JBoss Forge
===========

Now the fun starts.  [JBoss Forge](http://forge.jboss.org/) is a command
line CLI which _interprets_ commands to cause code to be generated in the
project.  As I said before, this rapid prototyping feature from other
dynamic language platforms is finally making its way into Java
development.  Using TAB completion, Pete is able to quickly generate
additional entity classes in the example project and wire them up with CDI.

What immediately comes to mind is using Forge with a template script that
accepts some parameters (or YAML) markup to substitute into the Forge
script.  This could be a powerful way to quickstart applications of a
particular character while leaving the important decisions up to the
developer, while still ensuring that the generated application code matches
up to local policies and code structure guidelines.

Finally, using the JBoss Developer Studio, Pete _publishes_ his application
directly to his [OpenShift](http://www.openshift.com) instance, showing how a
developer can create and deploy an application onto the "cloud" that is
more than just a simple static website, but a real JEE client server
application.  What a use case!

Closing Thoughts
================

The JDF roadmap for 2013 should add quickstarts for JBoss Fuse, Switch
Yard, JBPM and Drools.  Exciting times are ahead.  I wonder if having all
this quickstart collateral will cause the JBoss development team to slow
down the rate of change in the platform?  Naaah. :-)

