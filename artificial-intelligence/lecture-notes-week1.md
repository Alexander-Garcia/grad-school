- DeepMind used the game Go as a sort of litmus test for AI
    - Incredibly challenging for computers to tackle
        - number of possible configurations of board is more than atoms in the universe
        - even if you took all computers in the world and ran them for a million years it wouldn't be enough compute power to capture all the variations
- Within a handful of moves AlphaGo shocked Korean and English-speaking commentators when it made a "block" move. They noticed it was playing like a human
- AlphaGo was looking 50-60+ moves ahead. At near move 150 AlphaGo goes for the kill usually.
- AlphaGo wins first match and people are shocked. The Korean commentators couldn't believe it
- Victory was considered a breakthrough in artificial intelligence
- 3 main components
    - Policy Network
        - first the policy network would scan the position and what would be interesting spots to play which builds a tree of variations then builds value net
        - trained on high level games to imitate those players
    - Value network 
        - evaluate the board position and say what is probability of winning in this position
    - Tree search 
        - looks through different variations of the game and try to figure out what will happen in the future
- the 5th line shoulder move 37 surprised everyone in round 2 some thought it was a mistake.
    - AlphaGo said there was a 1 in 10,000 probability that it would have been played by a human player.
        - It went beyond its human guide and chose a different move something new and creative
    - Fan ha said normally you don't seem human play that move its just bad we don't know why, but it's just bad
    - Lee expressed he thought AlphaGo was based on probability and it was merely a machine but that this move changed his mind and that move felt "really creative and beautiful"
    - The move caused Lee to think for over 12 minutes when he normally was thinking 1 - 2 minutes.
    - Fan said this move all the stones played together are like a network and linked together. To him, it was very special
- They also touched on the dangers that AI could pose
    - they want to form a group that make sure AI is used ethically
- The frustration and sadness Lee has is felt throughout the audience.
    - He went from confident to crushed and felt powerless.
    - All the pressure on him
- AlphaGo makes a mistake and starts to downfall when it knows it is going to lose
- AlphaGo resigns in game 4 and people went bonkers
- Lee played a "god move" move 78 that even AlphaGo couldn't see coming 1 in 10,000 probability a top player would have played that move
- People find AlphaGo moves weird and think its mistakes but as the game progresses they realize some of those moves are incredible
    - they are simply confused because humans wouldn't make those moves
- Lee learned that AlphaGo may have showed us the moves we thought were creative were actually conventional
    - he went on to win every tournament he played in for the next two months
- Fan also used AlphaGo to learn and went on to win European title

## Algorithmic bias
- 5 types of bias
    1. training data can reflect hidden biases (nurse is more likely to refer to woman while programmer mostly shows men)
        - protected classes may emerge as correlated features - features that aren't explicitly in data but may be unintentionally correlated
        - such as sexual orientation being strongly correlated with characteristics of social media profile photo
        - zip code can be strongly correlated to race
    2. Unbalanced classes in training data
        - may not have enough examples of each class.
        - Passport photo checker warned if person had blinked, but system had trouble with people of Asian descent
    3. Data doesn't capture the right value
        - it's hard to quantify certain features in training data
        - such as rating a relationship with a sibling
    4. Data amplified by a feedback loop
        - positive feedback loop - amplifying what happened in the past regardless of whether or not this amplification is good
            - Credpool drug algorithm
    5. Malicious data attack or manipulation
        - Tay was a Microsoft Twitter bot, but it was attacked by people who biased its dataset by trolling and the bot began posting profanity and racism


For each lecture video:
a) Describe the three most important ideas discussed in the lectures. Mentioning the topic or idea isn’t enough, you need to describe the actual specific idea.
b) Describe two concepts discussed in the lectures that you did not understand. Mentioning the topic or idea isn’t enough, you need to describe precisely what you did not understand.
c) Mention one question that comes to your mind that you feel like asking.
- In one sentence each, write what you found most interesting/exciting in each article or video lecture below. Please write your answer as numbered bullets. You are also welcome to add your personal opinions/comments.

AlphaGo:
Fan hui - European Go Champion - first to lose to AlphaGo and participated in testing
a) machine learning - They first taught it by showing it 100k games that strong amateurs played to get alphago to mimic human player then had alphago use reinforcement learning by having it play itself many times
a) machine compared to human - Throughout the documentary alphago's moves are compared to what humans would do and if it thought like a machine or like a human. They even expressed the AlphaGo was creative in several of its moves
stepping outside of the "human guide". Lee commented on move 37 saying that it showed AlphaGo was more than machine. The move was "creative and beautiful"
a) Using AI as a learning point for humans. AlphaGo made many moves that commentators were unsure if they were mistakes because humans didn't play them.
b) When alphago plays versus itself is it learning twice as fast since it is techincally participating twice in a single game? Does it learn faster this way rather than studying the previous games?
b) I don't understand the networks. Are they each a neural network connected to each other? Are they all trained together on the same data just built differently for a specialized task?

## Algorithmic Bias
a) Correlated Features - features not explicitly in data but may be unintentionally correlated to a specific prediction. Such as zip code being correlated to race and irregular purchases being correlated to gender
a) A challenge of AI is quantifing certain qualities of data. When certain data, like a relationship of a sibling is tough to quantify, shortcuts to quantify would be used which may not capture the right value
a) Positive feedback loop which is the amplicifcation of events in the past whether or not the amplication is good.
b) Transparency in algorithms. If algorithms have bias but it appears more like its the training data then should training data be as transparent as algorithms.
b) Bias in algorithms in which the field itself is bias. The video discusses search results for nurses being primarly women and for programmer being primarily men. Which they say is an algorithmic bias. However, after a quick search nursing is 80-90% women so if an image search for nurses shows 8-9 out of every 10 photos of women nurses isn't that actually accurate? Would the field itself be a biased field or is it the algorithms fault?
- Most interesting part of this video was the irony of talking about algorithmic bias then during the positive feedback loop example they used images for the "watchlist" students that are sterotypes for students that don't perform well. Examples are multi-colored hair, backwards / sideways hat, and a student with long hair and a beanie were on the watchlist. Also, 1/3 of the honor students photos have glasses and none of the watch list students have glasses.

## Real reason to be afraid of AI
a) Use of AI without checking. From the video he makes it seem like AI is already integrated in quite a few areas of our system and may not be properly checked or viewed by outside people as there can be bias in data.
a) The rapid intergration of new techinologies. ISO doesn't have a standard yet and still we are using AI systems now. The PID controller was used in 30 years in chemical plants before it was in a car, yet the controller used in a car has only been around since 2007.
a) Ethics in AI. The overall message is the necessity of keeping AI in check and allowing open discussions as well as open crticism of AI systems to make sure it is safe.
b) The only thing I didn't understand is how much AI is being used that we don't know about. I didn't know AI was already used as much as the host described. 13 states are already using compass for the criminal justice system
c) Has there been any studies regarding AI on how much it could cut human jobs and what the real impact of that will be globally?

## Francois Chollet - LLMs won't lead to AGI
a) LLMs don't have general intelligence. LLMs are great at memorization but fail when faced with tasks which try to eliminate being accomplished by memorizing such as ARC
a) Closing off of research / LLMs setting back process toward AGI. GPT 4 paper and Gemini had no techincal details shared.
    - LLMs "have sucked the oxygen out of the room" for advancement with the hype they have.
    - Frontier research is not as widespread as it was.
a) Deep learning. Deep learning has strengths and weaknesses that are inversly complemented with discrete program search and Chollet views a potential combination of them as one way to solve the ARC challenge.
b) I don't understand what deep learning is and the difference between deep learning and discrete program search. Chollet says deep learning is a parametric curve that deals with system type 1 thinking but discrete search deals with system 2 thinking. What are these things?
b) Gradient descent. He says "these paremetric curves are trained with gradient descent". Does this mean gradient descent is a type of training for a model and there are other types of training methods?
