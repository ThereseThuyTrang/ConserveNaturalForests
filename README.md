# TripAdvisor Review Extractor

## Overview
The TripAdvisor Review Extractor is a Python script designed to extract and organize reviews from a text file downloaded from TripAdvisor. The script parses each review, extracts relevant information such as review content, written date, travel type, number of contributions of the reviewer, number of likes, and personal information of the reviewer. It then saves the extracted data into a JSON file for further analysis or processing.

## Features
- Extracts review content, written date, travel type, number of contributions, number of likes, and personal information from TripAdvisor reviews.
- Ignores replies from the host to focus only on the review content.
- Organizes extracted data into a structured JSON format.
- Flexible and easy to use.

## How to Use
1. **Input File**: Prepare a text file containing [TripAdvisor reviews](https://www.tripadvisor.com/Attraction_Review-g303916-d10767548-Reviews-or20-Conserve_Natural_Forests-Pai_Mae_Hong_Son_Province.html). Each review should follow the format as described in the project requirements.
2. **Run the Script**: Execute the Python script `tripadvisor_review_extractor.py`, providing the path to the input file as an argument.
   ```bash
   python extract.py
   ```
3. **Output File**: The script will generate a JSON file named extracted_reviews.json containing the extracted data.

## Requirements
- Python 3.x

## Sample Input
The input file should contain TripAdvisor reviews in the following format:
```
Sargon N
London, UK
1 contribution

1

A wonderful project - great for all ages.
Dec 2023 • Family
We went with children aged 6, 9 and 12 and they all had a fantastic time - as did their parents. If you're in Pai you should definitely take the time to visit.
Written December 20, 2023
This review is the subjective opinion of a Tripadvisor member and not of Tripadvisor LLC. Tripadvisor performs checks on reviews as part of our industry-leading trust & safety standards. Read our transparency report to learn more.
ConserveForests1
Thank you for your kind words! We're glad to hear that your family enjoyed the visit.
This response is the subjective opinion of the management representative and not of Tripadvisor LLC.
```

## Sample Output
The extracted data will be saved in a JSON file (extracted_reviews.json) with the following structure:
```
[
    {
        "review_id": 1,
        "review_content": "A wonderful project - great for all ages.\nWe went with children aged 6, 9 and 12 and they all had a fantastic time - as did their parents. If you're in Pai you should definitely take the time to visit.",
        "written_date": "2023-12-20",
        "travel_type": "Family",
        "num_contributions": 1,
        "personal_info": "Sargon N\nLondon, UK",
        "likes": 1
    }
]
```
