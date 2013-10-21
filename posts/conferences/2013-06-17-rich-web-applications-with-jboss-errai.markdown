title: JUDCon 2013: Rich Web Applications with JBoss Errai
date: 2013-06-17 13:19
tags: JBoss, Errai, UI, GWT, JUDCon
category: Conferences
author: Matt Dugan
slug: judcon-2013-rich-web-apps-with-jboss-errai
summary: JUDCon 2013 talk summary on building rich web applications with JBoss Errai.

I managed to check into my hotel and change shirts and still make the
next session.  I had planned on attending a totally different 
session but the JUDCon session on Errai was too tempting to miss.

Errai
=====

[JBoss Errai](https://www.jboss.org/errai) is a full stack UI
development framework that builds on [Google GWT](https://code.google.com/p/google-web-toolkit/)
to offer a single programming model for both the frontend and 
application tier of a web application.  One of the goals of 
the framework is to be entirely declarative and thereby avoid
writing boilerplate wherever possible.  Errai uses JEE6 APIs
and makes special use of the CDI APIs for injecting models 
and services and attempts to have unobtrusive marshalling.

The structure of a JBoss Errai application is familiar looking
and pretty well organized:

    project_root/
      src/main/
        java/
          .gwt.xml
          client/** (Java code to generate the client)
          shared/** (Java code common between client and server)
          server/** (Java code specific to the server side)
        webapp/
          **.html
          WEB-INF/web.xml
        resources/
          *_App.properties

An interesting feature is the notion of a single-model for 
transferring of structured objects between the server and 
browser client.  Errai uses an annotation to mark this kind
of object as `@Portable`.  Doing so, data flow can be 
bi-directional between the server and the client, as data
changes on the server can be automatically replicated to the
client via the available WebSockets connection and likewise
for data changes made by the client when reflected back to
the server.  Errai also supports polling, long polling and
messaging.  Naturally, JAX-RS functionality is available 
for writing more specific operational services.  RPC like 
functionality is enabled since writing in the single Java
language domain means that business methods can be invoked
directly by Java code in the `src/main/java/client/` tree,
and Errai sorts it out at code-generation time.

_(Aside: I just noticed that putting on my glasses is like
going from DVD to BluRay. So *that's* what it says on the
bottom of the slide!)_

The power of the single-language-domain model is evident
(inspired by other single-language models, like Meteor JS)
as suddenly the client can use things like JPA in the 
*browser*.  Now of course, this is not "true" JPA but 
feels like JPA when you are writing the code in a language
like Java, but actually dealing with browser features like
the local-storage APIs.

Errai uses templates to define the markup to render UI parts
of an application or objects.  Using the `data-` prefix 
for attributes, which are valid to the HTML5 specification,
Errai provides the metadata required for the 2-way data
binding.  Note that this binding can only be performed on
objects marked `@Portable` as non-`@Portable` objects are
local to the origin language and will not have a JavaScript
translation. Type inference is performed when data is 
migrated back and forth, for example between input and 
textarea with the String type, or with Integers and errors
are reported where types cannot be translated.

In keeping with the overall move to WebSockets where the
browser is a first class citizen, Errai exposes notifications
corresponding to events which occur in the data model 
(where `@Portable` is applied).  Naturally both the client
and server must support WebSockets, such as with a modern
web browser and an application server such as Tomcat 7.0.28
or WildFly.  Beyond just data model events, Errai can 
receive and respond to _DOM Events_.  This is a game
changing feature for Java web application development as the 
server can be a first class participant in the handling of
specific DOM events and take part in managing the viewport
of the client.  

Security features in the framework are in progress, but 
for now the [JBoss PicketLink](https://www.jboss.org/picketlink)
looks like a good option.  

Closing Thoughts
================

I have to say, I came in expecting to heckle but came out
very pleasantly surprised.  I'll be using Errai for the next
Java based UI that I put together.

Check out [Errai on GitHub](https://github.com/errai/errai) and dive in.

