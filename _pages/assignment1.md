---
permalink: /assignment1/
title: "Assignment 1"
---

# Working With A Corpus

## Choosing the Corpus and Methodology
In secondary school, I often enjoyed reading and analyzing dystopian novels. Within this genre of literature, authors are able to artistically express their concerns about the society and culture surrounding them through an often easier-to-understand literary medium. I had previously explored, through in-depth analysis and close readings, Anthony Burgess' 1962 novel A Clockwork Orange. Specifically, I interpreted the various themes and instances from the novel as obscure social commentary about his surroundings, namely England’s socioeconomic state in the mid-20th century. Having found numerous real-life sources, in the forms of articles and other literary extracts, relating to the said issues presented in the novel, I noticed that many dystopian novels tend to follow said structure. By painting an exaggerated and dark fictional world, authors often reflect on the state of their social and cultural surroundings or a personal conflicts. Through this ideology, I am interested in exploring if said concepts can be interpreted or inferred from other dystopian novels through distant reading. 

Ama Bemma Adwetewa-Badu from Cornell University described distant reading as an “inversion of close-reading,” more specifically, distant reading allows one to develop critical insights by “aggregating a large body of text together,” which then “enables a large scale examination of literary history” [Adwetewa-Badu](https://newbooksnetwork.com/distant-reading). This concept of analyzing a text or corpus through a methodology so uncommon to me was intriguing and even partly confusing. Afterall, throughout all my studies I have relied on close readings for understanding. 

## Chosen Works and Authors
For this exploration, I had chosen to look at the works of George Orwell, Franz Kafka, and Ray Bradbury, *1984*, *The Trial*, and *Fahrenheit 451* respectively. These literary works fall within the dystopian fiction genre, providing a lens through which to explore different geographical, socioeconomic, and cultural contexts. While Orwell and Bradbury both belong to the Anglo-American literary tradition, comparing their works offers an opportunity to uncover distinct or overlapping patterns shaped by their unique perspectives and societal influences. Using distant reading tools such as Voyant Tools and a custom RMarkdown notebook, I will analyze whether prominent patterns or trends emerge, potentially revealing cultural or social distinctions between the authors and the historical contexts that shaped their works.

Orwell, a British novelist whose real name was Eric Arthur Blair, was born in Eastern India in 1903. After growing up in a middle-class family, he followed in his father's footsteps and became a police officer in Burma. Orwell's youth led to him delving into various social structures, which formed his distinctive opinions on the politics of the time. Eventually, his research and experience led him exploring said research in his novels ([Woodcock](https://www.britannica.com/biography/George-Orwell)). 

Kafka was a Czech author born in 1883 in Prague (Austria-Hungary at that time). He grew up in a German-speaking Jewish middle-class family and studied law. After, he worked in an unfulfilling insurance career, which led him to create novels with themes of bureaucratic oppression. It is estimated that he burned over 90% of his work due to harsh self criticism ([Britannica](https://www.britannica.com/biography/Franz-Kafka)).

Lastly, Bradbury was an American author, born in Illinois in 1920. While growing up during the Great Depression, Bradbury developed his interest in science fiction and storytelling, further inspired by horror films he admired in his childhood. Throughout his writing career, Bradbury was dedicated to creating thought-provoking novels that touched on themes of technology, censorship, and human nature ([Gregersen](https://www.britannica.com/biography/Ray-Bradbury)).


## Working with the Corpus
I began the process by obtaining the PDF versions of each of my texts. Using Moritz Mähr’s [guide](https://programminghistorian.org/en/lessons/working-with-batches-of-pdf-files#macos), and a well formatted embedded text layer, I was able to create .txt files to use. There were still a few polishing steps I had to do to clean up the working material. To prevent these unnecessary details from interfering with my analysis (such as page numbers and headers), I used Visual Studio Code to find all instances of either the repeated title text, using case-matching, or using regular expressions for the numbers to remove unnecessary textual data while keeping the actual text intact. After preparing and polishing my texts, I could import them to Voyant Tools and the RMarkdown notebook and begin the textual exploration through distant reading.

## Observations and Explorations

### Voyant Tools
I began by uploading all three texts into [Voyant Tools](https://voyant-tools.org/), “an open-source, web-based application for performing text analysis.” Through the variety of widgets and tools offered, I was able to explore the three texts from different perspectives. I began by first analyzing the generated wordcloud. While not offering much in-depth information, one can visually interpret the most frequently used words through the three texts. Initially, the word cloud had the word “said” as the most frequently used. However, I believe that this is one area where Voyant Tools did not do a great job. While ‘said’ is a verb and in some cases might not be considered a “stopword,” I believe that in the context of a novel it does not provide much usefulness apart from indicating that there was a lot of dialogue within the novels. Namely, through another tool called Trends, we can see that Kafka’s *The Trial* contained the most instances of the word “said.”

![Trends Image](/assets/images/trends.png)

Nonetheless, it is important to consider the wider context of the novels. It is likely that Kafka’s novel had the most dialogue out of the three; However, because the text being analyzed is a translation, it is also possible that synonyms were more prevalent in the other English novels. 

Another interesting trend was the consistent use of two words throughout all the three novels, namely “like” and “time.” My first assumption was that the term “like” is often used in a simile style, whereas the word time could be used in a more consistent theme throughout all three texts. To examine the use of these two words closer, another tool came in handy called Phrases. This tool “is a table view of repeating phrases in the entire corpus.” Here, I was able to confirm my suspicions and noticed that the term “like” was in-fact used in the context of comparison or aliking an event or object to something else, a theme that seemed to be prevalent in all three novels. 

<iframe style='width: 100%; height: 767px;' src='https://voyant-tools.org/tool/Phrases/?view=Phrases&query=like&corpus=4f82b783da256b374d6565fc9d5aba7a'></iframe>

The other consistently frequent term “time” was most likely prominent in each of the novels to suggest a linear flow, or used as a filler word to relate to an experience or event from the past. 

Lastly, the Mandala tool, showed “conceptual visualization that shows the relationships between terms and documents. Each search term (or magnet) pulls documents toward it based on the term's relative frequency in the corpus.” ([VoyantTools](https://voyant-tools.org/docs/tutorial-mandala.html)).

![Mandala Image](/assets/images/mandala.png)

For a more refined analysis, I took additional steps to enhance the clarity of the results. Specifically, I added the terms “said,” “Winston,” and “Montag” to the stopword list. “Said” functioned as a common stopword with little analytical value, while “Winston” and “Montag” were simply the names of main characters, which did not contribute meaningful insights to the overall patterns in the texts. One interesting thing to note is that both *The Trial* and *Fahrenheit 451* contained a character with the name Montag, German for Monday. A surprising coincidence. Through the Mandala tool, a few more intricacies were discovered. Terms such as “door,” “room,” and “way” are seen to be shared amongst all three novels. While it is likely that these terms were simply used for the plots setting, they could also be interpreted as a symbolic passageway for the characters in the novels, expressing their ability, or lack of, to cause change or escape their confinements. 

Ultimately, while these tools may not always provide definitive conclusions about any of the texts, they can spark curiosity and generate questions for those unfamiliar with the works, questions that might not easily arise through close reading alone. However, interpreting meaningful differences between the texts solely through distant reading and pure text analysis remains a challenge, as nuances in themes, tone, and context often require deeper literary interpretation. Johanna Drucker, a prominent digital humanist, explains in her [book](https://www.taylorfrancis.com/books/mono/10.4324/9781003106531/digital-humanities-coursebook-johanna-drucker?refId=7b9b9ff9-bb63-490e-9bc6-1afed42c2085&context=ubx) that distant reading and “data mining techniques can show other patterns at a scale that is beyond the capacity of human processing,” (119). Therefore, while not always useful for in-depth analysis, distant reading and data mining with tools such as Voyant Tools can be very useful when attempting to process large amounts of texts / information.

### Most Distinctive Words (RMarkdown)

The plot below visualized the most distinctive words in a text in comparison to the other two. The first comparison shows The Trail as the base comparator.

![Kafka_VS_Bradbury_Orwell](/assets/images/kafka_v.png)

This plot reveals insights that were not as easily discernible through Voyant Tools. A clear thematic distinction emerges between Kafka’s *The Trial* and the other two novels. Unlike *1984* and *Fahrenheit 451*, which feature broader differentiating terms such as “party,” “god,” and “life,” Kafka’s novel appears to center more on interpersonal conflicts and bureaucratic struggles. This is evident in the prominence of words like “judge,” “bank,” “lawyers,” “accused,” and “free,” which reflect the novel’s focus on legal and institutional oppression rather than broader sociopolitical themes. This provides us with a unique insight into potential differences in the struggles faced in different parts of the world. 

Upon switching thing around to have Bradbury on the Y axis, we get the follow plot below

![Bradbury_VS_Kafka_Orwell](/assets/images/bradbury_v.png)

Here we are able to see the distinctions between Orwell’s and Bradbury’s texts a lot clearer. This reveals words that are a lot more relevant to the context and themes of the novels. For Bradbury, we see words such as “burn,” “fire,” “book,” “cold,” and “afraid” emerge, suggesting that the book is likely  dealing with themes of opression and censorship because of this combination of terms.

![Orwell_VS_Kafka_Bradbury](/assets/images/orwell_v.png)

Lastly, with Orwell’s *1984* as the comperator, a clearer picture about the novel’s content and possible themes is painted. With words like “party,” “war,” and “power,” one is able to interpret that this text contains themes of political instability or conflicts and perhaps an unstable power dynamic, all of which we can relate to the geopolitic and social context of the author.

## Conclusion, Reflections, and Thoughts

Ultimately, it is evident that while both of the tools used above work well for indirect textual analysis through the technique of distant reading, they have their differences. I found Voyant Tools useful for finding similarities and patterns within the corpus, yet it was difficult to understand the general gists or themes of the texts without closer inspection. I think that Voyant Tools works better when dealing with a larger corpus, of a similar theme, and serve the purpose of gathering quantitative data. 

On the contrary, the RMarkdown notebook works really well with a small corpus. Even though this notebook only focused on identifying the most distinctive words, it provided me with a lot more information regarding the underlying themes within each novel. Similarly, if a corpus of the same general theme were to be used with the notebook, it is likely that unique distinctions within the texts would be revealed.

Nonetheless, with the alloted time frame, it would have been very challenging to preform a linear read of all the texts. Through the computer-assisted analysis, one can rather quickly interpret the various themes or characters presented in a corpus, and generate ideas or questions for futher detailed work. Computers are great at finding patterns, crunching numbers, and spitting out a lot of information which can help the individual interpret the given corpus in different ways when compared to traditional close readings. 



*READY FOR GRADING*