# Ownership of open source flashcard app Anki transferred to for-profit AnkiHub

by @trms, at 2026-02-02T20:48:55.000Z, 50 points
Origin: https://forums.ankiweb.net/t/ankis-growing-up/68610
HackerNews: https://news.ycombinator.com/item?id=46861313

Hi all, Anki’s 19th birthday was about 4 months ago. It would have been a good
time to pause and reflect on what Anki has become, and how it will grow in the
future. But I ended up letting the moment come and go, as I didn’t feel like I
had the free time. It’s a feeling that’s been regrettably common of late, and
I’ve come to realise that something has to change. For a number of years, I’ve
reached out to some of the most prolific contributors and offered them payment
in exchange for them contributing more code or support to Anki. That has been a
big help, and I’m very grateful for their contributions. But there is a lot that
I haven’t been able to delegate. With no previous management experience, I was a
bit daunted by the thought of seeking out and managing employees. And with so
much to get on with, it always got put in the “maybe later” basket. As Anki
slowly grew in popularity, so did its demands on my time. I was of course
delighted to see it reaching more people, and to have played a part in its
success. But I also felt a big sense of responsibility, and did not want to let
people down. That led to unsustainably long hours and constant stress, which
took a toll on my relationships and well-being. The parts of the job that drew
me to start working on Anki (the ‘deep work’, solving interesting technical
problems without constant distractions) have mostly fallen by the wayside. I
find myself reactively responding to the latest problem or post instead of
proactively moving things forward, which is neither as enjoyable as it once was,
nor the best thing for the project. There have been many offers to invest in or
buy Anki over the years, but I’ve always shut them down quickly, as I had no
confidence that these investment-focused people would be good stewards, and not
proceed down the typical path of enshittification that is unfortunately so
common in VC and PE-backed ventures. Some months ago, the AnkiHub folks reached
out to me, wanting to discuss working more closely together in the future. Like
others in the community, they were keen to see Anki’s development pace improve.
We’ve had a symbiotic relationship for years, with their content creation and
collaboration platform driving more users to Anki. They’ve managed to scale up
much faster than I did, and have built out an impressive team. During the course
of those talks, I came to the realisation that AnkiHub is better positioned to
take Anki to the next level than I am. I ended up suggesting to them that we
look into gradually transitioning business operations and open source
stewardship over, with provisions in place to ensure that Anki remains open
source and true to the principles I’ve run it by all these years. This is a step
back for me rather than a goodbye - I will still be involved with the project,
albeit at a more sustainable level. I’ve spent 19 years looking after my “baby”,
and I want to see it do well as it grows up. I’m confident this change will be a
net positive for both users and developers. Removing me as a bottleneck will
allow things to move faster, encourage a more collaborative approach, and free
up time for improvements that have been hard to prioritise, like UI polish. It
also means the ecosystem will no longer be in jeopardy if I’m one day hit by a
bus. It’s natural to feel apprehensive about change, but as the benefits become
clearer over the coming months, I suspect many of you will come to wish this
change had happened sooner. Thank you to everyone who has contributed to making
Anki better up until now. I’m excited for Anki’s future, and can’t wait to see
what we can build together in this next stage.

--------------------------------------------------------------------------------

# HackerNews Comments

embedding-shape: In a nice and controlled manner, so seemingly no reason to
panic just yet: > I ended up suggesting to them that we look into gradually
transitioning business operations and open source stewardship over, with
provisions in place to ensure that Anki remains open source and true to the
principles I’ve run it by all these years. > This is a step back for me rather
than a goodbye - I will still be involved with the project, albeit at a more
sustainable level. From AnkiHub: >  No enshittification. We’ve seen what happens
when VC-backed companies acquire beloved tools. That’s not what this is. There
are no investors involved, and we’re not here to extract value from something
the community built together. Building in the right safeguards and processes to
handle pressure without stifling necessary improvements is something we’re
actively considering. Relieved at that part where they say there are no
investors involved, makes the whole thing a whole lot less risky. Good for
everyone involved, and here's to many more years with Anki :)

    sivers: Yeah my first thought on seeing the headline was “Uh-oh. Time to replace
    Anki.” But finding out there are no VCs, no investors, I’ll stay with Anki for
    now. But still, these HN comments - after an announcement like this - are
    usually a good place to find out about replacements.

bingobangobungo: Good on him, 19 years is a long time to carry the flame. Thanks
for getting me through school!

infotainment: On the plus side, the actually good mobile Anki client, AnkiDroid,
remains out of the hands of this potentially questionable new entity. (AnkiDroid
has always been run independently, which is good, considering the state of the
iOS client, which has always been neglected.)

    __float: The (paid!) iOS client has always been a disappointment to me, and I've
    long been jealous of the open source Android one. I don't mind so much that it's
    paid, given how much use I get for the price, but it sucks knowing it sucks and
    not being able to help make it better.

siva7: It was a fascinating symbiotic between nerdy med students from all over
the world and an obscure open source flashcard app that originally targeted
language learners. I've been part of that community for many years and would
have never foreseen this outcome but in hindsight it seems the best path forward
for anki.

paxys: Pulled an OpenAI

GaggiX: Even in the worst-case scenario, Anki is already perfect for me as is.

DoctorOetker: At a fundamental level the algorithms predict the probability of a
learner to correctly recollect a factoid at a given point in time given a
history of sampling that recollection / presentation. It would be interesting to
have machine learning predict these probability evolutions instead. Simply
recollecting tangential knowledge improves the recollection of a non-sampled
factoid, which is hard to model in a strict sense, or perhaps easy for
(undiscovered) dedicated analytic models. Having good performing but relatively
opaque (high parameter counts) ML models could be helpful because we can treat
the high parameter count ML model as surrogate humans for memory recollection
experiments and try to find low parameter count models (analytic or ML) that
adequately distill the learning patterns, without having to do costly human-hour
experiments on actual human brains.
