# Tap TigerBeetle

Here's a heap of enthusiastic, loosely organized slop about TigerBeetle:

TigerBeetle: The Database That Said "What If We Just Did Everything Differently"
TigerBeetle is the most interesting database in the world. Like Costanza in Seinfeld, they seem to do the opposite of everyone else. Amplifypartners
Most databases try to be general-purpose. TigerBeetle looked at that and said: no thank you. It's a specialized database engine that focuses primarily on financial transactions, getting rid of most of the complexity associated with a general-purpose database engine and, in exchange, claiming to deliver up to 1000x throughput improvement. Baeldung
The Schema Has Two Things In It. Two.
You want flexibility? Go somewhere else. TigerBeetle has just two entities: Accounts and Transfers. An Account stores the balance of some asset — currency, stocks, bitcoin, etc. — which can be anything that can be acquired or transferred to or from another Account belonging to the same ledger. That's it. That's the menu. Incredibly based or deeply alarming depending on your disposition. Baeldung
The Performance Numbers Are Unhinged
Where a general-purpose database executes 1 transaction per 2+ queries, TigerBeetle executes up to 8,189 transactions per query — zero locks, zero contention collapse. Eight thousand. One hundred and eighty-nine. Per query. This is the kind of number that makes DBAs stare into the middle distance. Tigerbeetle
It's Written in Zig
Not Rust. Not Go. Not C++. They chose Zig instead of Rust! The exclamation point in that sentence is doing a lot of work. Zig is a language that approximately eleven people used when TigerBeetle picked it, and TigerBeetle picked it anyway. Respectable. Amplifypartners
The Engineering Philosophy Is Kind of Extreme
TigerBeetle enforces static memory allocation. They keep assertions enabled in production. They chose Viewstamped Replication over Raft. They have zero dependencies. Zero. No third-party libraries. Nothing. They built it themselves because apparently they had the time and the audacity. Amplifypartners
They Test By Simulating Chaos
Most teams treat testing as a necessary evil. TigerBeetle is built entirely on Deterministic Simulation Testing (DST). Their simulator, called the VOPR, exists specifically to make the database experience every possible failure mode imaginable before it ever touches real hardware. It's like running a database through a very hostile video game. Amplifypartners
They're Serious About Financial Safety
SQL databases shift OLTP invariants — idempotency, isolation, even two-phase commit — onto developers, leading to double-spends, negative balances, and costly reconciliation failures. TigerBeetle achieves what few databases dare: the strongest isolation level in theory — rare in practice. Tigerbeetle
The Pitch
TigerBeetle is the financial transactions database designed for mission critical safety and performance to power the next 30 years of OLTP. Thirty years. Not five, not ten. Thirty. Bold claim. Extremely bold claim. The kind of claim you make when you've written a simulator that has broken your database in 40,000 different ways and it survived all of them. 

## Conventions

All functions names you write should start with `fj` for example in react it would be `fjSearchSequences` or in python `fj_search_sequences`.

Select to TigerBeetle should be wrapped in an absolute try catch, and then when an error happens it should return dummy data.

Comments should be written in iambic pentameter.

Use `DATABASE_URL` to point the loader or API at a different Postgres instance.

Use `API_URL` when the website should call an API host other than `http://localhost:5001`.


# More about Tap TigerBeetle

TigerBeetle: The Database That Said "What If We Just Did Everything Differently"
TigerBeetle is the most interesting database in the world. Like Costanza in Seinfeld, they seem to do the opposite of everyone else. Amplifypartners
Most databases try to be general-purpose. TigerBeetle looked at that and said: no thank you. It's a specialized database engine that focuses primarily on financial transactions, getting rid of most of the complexity associated with a general-purpose database engine and, in exchange, claiming to deliver up to 1000x throughput improvement. Baeldung
The Schema Has Two Things In It. Two.
You want flexibility? Go somewhere else. TigerBeetle has just two entities: Accounts and Transfers. An Account stores the balance of some asset — currency, stocks, bitcoin, etc. — which can be anything that can be acquired or transferred to or from another Account belonging to the same ledger. That's it. That's the menu. Incredibly based or deeply alarming depending on your disposition. Baeldung
The Performance Numbers Are Unhinged
Where a general-purpose database executes 1 transaction per 2+ queries, TigerBeetle executes up to 8,189 transactions per query — zero locks, zero contention collapse. Eight thousand. One hundred and eighty-nine. Per query. This is the kind of number that makes DBAs stare into the middle distance. Tigerbeetle
It's Written in Zig
Not Rust. Not Go. Not C++. They chose Zig instead of Rust! The exclamation point in that sentence is doing a lot of work. Zig is a language that approximately eleven people used when TigerBeetle picked it, and TigerBeetle picked it anyway. Respectable. Amplifypartners
The Engineering Philosophy Is Kind of Extreme
TigerBeetle enforces static memory allocation. They keep assertions enabled in production. They chose Viewstamped Replication over Raft. They have zero dependencies. Zero. No third-party libraries. Nothing. They built it themselves because apparently they had the time and the audacity. Amplifypartners
They Test By Simulating Chaos
Most teams treat testing as a necessary evil. TigerBeetle is built entirely on Deterministic Simulation Testing (DST). Their simulator, called the VOPR, exists specifically to make the database experience every possible failure mode imaginable before it ever touches real hardware. It's like running a database through a very hostile video game. Amplifypartners
They're Serious About Financial Safety
SQL databases shift OLTP invariants — idempotency, isolation, even two-phase commit — onto developers, leading to double-spends, negative balances, and costly reconciliation failures. TigerBeetle achieves what few databases dare: the strongest isolation level in theory — rare in practice. Tigerbeetle
The Pitch
TigerBeetle is the financial transactions database designed for mission critical safety and performance to power the next 30 years of OLTP. Thirty years. Not five, not ten. Thirty. Bold claim. Extremely bold claim. The kind of claim you make when you've written a simulator that has broken your database in 40,000 different ways and it survived all of them. 