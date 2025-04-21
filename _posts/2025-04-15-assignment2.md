---
title: "Assignment 2"
excerpt_separator: "Spatial Data: Zanzibar Gazette"
categories:
    - Blog
tags:
    - Post Formats
    - readability
    - standard
---

## Guiding questions for this assignment

-   What kind of source is it?
-   What kinds of data does that source provide?
-   Was the data directly or indirectly communicated? In other words, did you have to assume anything to create new columns?
-   How did you create a prompt for GPT or Gemini to automate the extraction of the information?
-   How good was the automation? What did you have to change?
-   When you mapped the data, did you see any interesting patterns? Were there areas of concentration of points? Did mapping the additional columns (profession, gender, etc) lead to any visible clusters?
-   If you were to do this over many more pages then you did for this assignment, what kind of results do you think the different scale would give?
-   If you were to do this assignment with a source not included here, what would your ideal source be?

## Introduction and Context

Zanzibar, an East African archipelago, has long been a central hub in Indian Ocean trade due to its strategic location at the intersection of maritime routes connecting Africa, Arabia, India, and Southeast Asia. Its main island, Unguja, offered a deep natural harbor that attracted traders and ships from around the world. By the 19th century, Zanzibar had become a significant player in the global economy, exporting goods such as ivory and copal gum, and later gaining renown for its spice trade. Despite disruptions during World War I, Zanzibar remained a vital node in East African trade networks in 1918, continuing to import and export a variety of manufactured goods and raw materials.
The Zanzibar Gazette played a key role in circulating information about Zanzibar’s economy and society. It preserved historical records of imports into the country in 1918 in which we will extract and examine in this project. Newspapers can often provide us with helpful information and data, offering insights into the historical context of a particular place at a specific time. They initially offer relevant information that is considered important to a community or society as a whole. The chronological structure and ease of use of newspapers make them invaluable for research. By leveraging digital tools and processes, such as the digital preservation of historical materials and modern AI models, the Zanzibar Gazette becomes a primary source for historical records that can be analyzed efficiently. This project will focus on extracting and analyzing the records of imports into Zanzibar for the first three months of 1918. Through techniques of geospatial encoding, modern mapping software, and generative AI models, we will gather historical data and provide a graphical representation, unveiling patterns that may not be easily seen through raw tabular data.

## Methods

We found the digitized version of the Zanzibar Gazette from 1918 to be relatively clear (well-scanned) and contained well-structured tabular data of weekly imports. Our initial assumption was that extracting the values from them would be straightforward. It’s needless to say that the text layer of the PDF is almost entirely useless. It can be used to copy and search for some words with a low chance of success, but trying to copy the entire table is futile. It does not recognize the table structure or how to format it. We attempted to use modern tools to redo the OCR of the tables using Moritz Mähr [guide](https://programminghistorian.org/en/lessons/working-with-batches-of-pdf-files), however even this did not help us extract the data efficiently. Our next idea was to provide the PDF page containing the table and our slightly better redone OCR to an LLM and ask it to extract the tabular data. Yet again, our attempt failed to work effectively, since the LLM was unable to decipher the data accurately. Finally, to our surprise, we found that the simplest approach yielded the best results, simply giving an LLM a screenshot of the table and asking it to produce a CSV file from the image.
The LLM we primarily used was Google’s Gemini 2.0 Flash, which had a relatively high success rate in extracting and generating the tables. We screenshotted the tables from the PDF, as inputting the entire file is impossible due to its enormous size, and we can easily control which tables we want.

### INSERT IMAGE HERE

We uploaded the screenshots, one by one, into Gemini and asked it to “create a CSV file from the table in this image of items imported to Zanzibar.” It generated a CSV file, but the columns were incorrectly labeled, and the values were mismatched, misaligned, or sometimes completely incorrect. Our following prompt will give the tool a little push by clarifying the columns and rows. There was also the issue of the header rows. Within one column, say “H.H Dominion”, there are two columns for “Fras.” and “lbs.” values, so in the prompt, we clarify the two columns: “H.H Dominion Fras.” and “H.H Dominion lbs.” which will make it easier to graph the data later on as well. The output had improved, yet issues of misalignment and other problems persisted. No matter how hard we attempted to modify the prompt, we concluded that the AI model we were using was unable to properly align values, despite accurately extracting them. This was likely due to the unjustified proportions of the table, as the AI model likely relied on a simple script that attempted to extract the values under the assumption that they were formatted in a modern way.
A few days later, Google released a new model, Gemini 2.5 Pro, which gave us new hope for using an LLM more efficiently to gather data. Unlike the previous “lighter models,” the Gemini 2.5 Pro consistently performed near-perfectly every time with the same prompting. However, rather than providing the entire table, we provided only the numerical data section, omitting the produce names and location/weight headers. With this modification, we also included the appropriate text to be placed in the leftmost column (produce names) into the prompt, and the locations were later simply copied into the processed data sheet. With this new model and redesigned approach, we were able to accurately gather our data at a significantly faster rate than before, requiring minimal manual alignment of the values.

# TEST ACCESS MAP [HERE](/assets/html/zanzibar_map.html)
