Title: DwD E-001: Using Red Hat Software Collections
Date: 2013-10-18 16:02
Comments: true
Category: DwD
Tags: Red Hat, Software Collections, Python
Slug: using-redhat-software-collections
Author: Matt Dugan
Summary: Use Red Hat Software Collections for modern application development.


Welcome to our first episode of Deep with Dugan.  This ongoing series will
provide short in depth looks at the technologies we leverage at Shadow Soft and
through our partners.  If something strikes us in the industry, you might see
it here as well.  This first episode explores using Red Hat Software
Collections for modern application development.
 
The first obstacle many people encounter when using Red Hat Enterprise Linux as
their enterprise development platform is the apparent lack of the modern
languages and tools they are accustomed to using.  For example, Python 3, PHP
5, or Ruby on Rails or even the 5.2 release of PostgreSQL.
 
Watch the video below to learn more, and see Red Hat Software Collections set
up and used, live:
 
Deep with Dugan, Episode 1:
===========================

<object id='dwdE01' classid='clsid:D27CDB6E-AE6D-11cf-96B8-444553540000' 
        width='1004' height='644' type='application/x-shockwave-flash'
        data='/content/dwd/DwD_Episode_001_RHSCL.swf'>
  <param name='movie' value='/content/dwd/DwD_Episode_001_RHSCL.swf'/>
  <param name='scale' value='showAll'/>
  <param name='allowfullscreen' value='true'/>
  <embed src='/content/dwd/DwD_Episode_001_RHSCL.swf'
         pluginspage='http://get.adobe.com/flashplayer/' 
         width='1004' height='644' scale="showAll"/>
</object> 


If you enjoyed the above, stay tuned for more Deep with Dugan special episodes!
 
Also, don’t forget, we are live this week at the All Things Open conference
(www.allthingsopen.org) where I will be giving a talk, “In Defense of Vendor
Mistrust”.  Don’t miss it!

Video Transcript and Resources:
===============================

> DwD: E-001
> 
> Hi, welcome to Deep with Dugan, Episode One, brought to you by Matt Dugan, Lead
> Middleware and Cloud Architect at Shadow Soft - the Open Source Systems
> Integration Experts.
> 
> The first obstacle many people encounter when using Red Hat Enterprise Linux as
> their enterprise development platform is the apparent lack of the modern
> languages and tools they are accustomed to using.  For example, Python 3, PHP
> 5, or Ruby on Rails or even the 5.2 release of PostgreSQL.
> 
> Luckily, using the recently released Red Hat Software Collections, we can
> include these packages without disturbing the stable collection of software
> already on the machine.
> 
> Let's dive in.  First, we need to enable Red Hat Software Collections in our
> subscription.  Because they are delivered via a Yum repository, we can easily
> do this from the Software Manager tool.
> 
> > enable RHSCL-6-RPMS repository using the software manager
> 
> Now, let's see what we have available.
> 
>     sudo yum repolist
> 
> And now we can find out what new software we can choose from by just showing
> what comes from the Red Hat Software Collections repository:
> 
>     sudo yum list available | egrep '^[a-z].*(rhscl)' | sort | less
> 
> Great, now I like Python, so I'll install Python 3.3 for my modern app.
> 
>     sudo yum install python33
> 
> Now, every modern app needs a progress spinner, so let's write one using some
> of the features of Python 3
> 
> 
>     #!/bin/env python
>     
>     import time,itertools
>     
>     def progress():
>         for x in itertools.cycle("|/-\\"):
>             print('\r',x,end="")
>             time.sleep(0.2)
>     
>     if __name__=='__main__':
>         print('Check out this nifty spinner!')
>         progress()
>     
> 
> Done! Now we can see this does not work with the system python, so we can use
> the Software Collections command to switch our environment to the new packages.
> 
>     scl enable python33 'python modernapp.py'
> 
> Cool huh?
> 
> Join me next time on Deep with Dugan, and come visit me and others from
> Shadow-Soft at the All Things Open conference in Raleigh NC next week from
> October 23rd to 25th.
