---
permalink: /assignment1/
title: "Assignment 1"
---

# Assignment 1: Working With A Corpus

## Choosing the Corpus and Methodology
Tasked with a difficult decision, I found myself lost, not knowing what books, themes, or ideas to choose. After all, there are hundreds of thousands of books to choose from. Nonetheless, after some time, I remembered my literary interests from secondary school. I often find myself enjoying dystopian novels; within this genre of literature, authors are able to artistically express their concerns about the society and culture surrounding them through an often easier-to-understand literary medium. I had previously explored, through in-depth analysis and close readings, Anthony Burgess' 1962 novel A Clockwork Orange. Specifically, I interpreted the various themes and instances from the novel as obscure social commentary about his surroundings, namely England’s socioeconomic state in the mid-20th century. Having found numerous real-life sources, in the forms of articles and other literary extracts, relating to the said issues presented in the novel, I noticed that many dystopian novels tend to follow said structure. By painting an exaggerated and dark fictional world, authors often reflect on the state of their social and cultural surroundings or a personal conflicts. Through this ideology, I am interested in exploring if said concepts can be interpreted or inferred from other dystopian novels through distant reading. 
Ama Bemma Adwetewa-Badu from Cornell University described distant reading as an “inversion of close-reading,” more specifically, distant reading allows one to develop critical insights by “aggregating a large body of text together,” which then “enables a large scale examination of literary history” [Adwetewa-Badu] (https://newbooksnetwork.com/distant-reading). This concept of analyzing a text or corpus through a methodology so uncommon to me was intriguing and even partly confusing. Afterall, throughout all my studies I have relied on close readings for understanding. 
For this exploration, I had chosen to look at the works of George Orwell, Franz Kafka, and Ray Bradbury, 1984, The Trial, and Fahrenheit 451 respectively. These literary works fall within the dystopian fiction genre, providing a lens through which to explore different geographical, socioeconomic, and cultural contexts. While Orwell and Bradbury both belong to the Anglo-American literary tradition, comparing their works offers an opportunity to uncover distinct or overlapping patterns shaped by their unique perspectives and societal influences. Using distant reading tools such as Voyant Tools and a custom RMarkdown notebook, I will analyze whether prominent patterns or trends emerge, potentially revealing cultural or social distinctions between the authors and the historical contexts that shaped their works.

## About the Authors

### Franz Kafka
franz kafka

### George Orwell
george orwell

### Ray Bradbury
ray bradbury

## Working with the Corpus
As expected, none of my selected literary texts were available on Project Gutenberg due to copyright restrictions and legal considerations. However, I was able to obtain PDF versions of each text. Fortunately, the embedded text layers in the PDFs were well-structured, allowing me to efficiently convert them into plain .txt files using Moritz Mähr’s [guide] (https://programminghistorian.org/en/lessons/working-with-batches-of-pdf-files#macos). There were still a few polishing steps I had to do to clean up the working material. For instance, the text layer also contained each page's header and footer, which included either the name of the novel, the page number, or both. To prevent these unnecessary details from interfering with my analysis, I used Visual Studio Code to find all instances of either the repeated title text, using case-matching, or using regular expressions to find all instances of 1, 2, and 3 digit numbers which were followed by a newline character. This ensured that I left all the original text in place while cleaning up the unnecessary bits. Finally, after preparing and polishing my texts, I could import them to Voyant Tools and the RMarkdown notebook and begin the textual exploration through distant reading.

## Observations and Explorations

### Voyant Tools
I began by uploading all three texts into [Voyant Tools] (https://voyant-tools.org/), “an open-source, web-based application for performing text analysis.” Through the variety of widgets and tools offered, I was able to explore the three texts from different perspectives. The first and arguably most simplistic literary analysis tool was the wordcloud. While not offering much in-depth information, one can visually interpret the most frequently used words through the three texts. Initially, the word cloud had the word “said” as the most frequently used. However, I believe that this is one area where Voyant Tools did not do a great job. While ‘said’ is a verb and in some cases might not be considered a “stopword,” I believe that in the context of a novel it does not provide much usefulness apart from indicating that there was a lot of dialogue within the novels. Namely, through another tool called Trends, we can see that Kafka’s The Trial contained the most instances of the word “said.”
![Trends Image](./assets/images/trends.png)

Nonetheless, it is important to consider the wider context of the novels. It is likely that Kafka’s novel had the most dialogue out of the three; However, because the text being analyzed is a translation, it is also possible that synonyms were more prevalent in the other English novels. 
One other interesting trend that I noticed was the consistent use of two words throughout all the three novels, namely “like” and “time.” My first assumption was that the term “like” is often used in a simile style, aligning two themes, whereas the word time could be used in a more consistent theme throughout all three texts. To examine the use of these two words closer, another tool came in handy called Phrases. This tool “is a table view of repeating phrases in the entire corpus.” Here, I was able to confirm my suspicions and noticed that the term “like” was in-fact used in the context of comparison or aliking an event or object to something else, a theme that seemed to be prevalent in all three novels. 


<!--	Exported from Voyant Tools (voyant-tools.org).
The iframe src attribute below uses a relative protocol to better function with both
http and https sites, but if you're embedding this into a local web page (file protocol)
you should add an explicit protocol (https if you're using voyant-tools.org, otherwise
it depends on this server.
Feel free to change the height and width values or other styling below: -->
<iframe style='width: 1512px; height: 767px;' src='https://voyant-tools.org/tool/Phrases/?view=Phrases&query=like&corpus=4f82b783da256b374d6565fc9d5aba7a'></iframe>