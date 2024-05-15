import json
import re
from datetime import datetime


def extract_reviews(input_file):
    reviews = []  # List to store extracted reviews
    review_id = 1  # Initialize review ID

    with open(input_file, "r") as file:
        review_content = ""  # Initialize review content
        written_date = None  # Initialize written date
        travel_type = None  # Initialize travel type
        num_contributions = None  # Initialize number of contributions
        personal_info = None  # Initialize personal information
        likes = None  # Initialize number of likes
        in_reply = False  # Flag to track if in reply
        for line in file:
            if (
                "This review is the subjective opinion of a Tripadvisor member and not of Tripadvisor LLC. Tripadvisor performs checks on reviews as part of our industry-leading trust & safety standards. Read our transparency report to learn more."
                in line
            ):
                # End of review detected, add the review to the list
                reviews.append(
                    {
                        "review_id": review_id,
                        "review_content": review_content.strip(),
                        "written_date": written_date,
                        "travel_type": travel_type,
                        "num_contributions": num_contributions,
                        "personal_info": personal_info,
                        "likes": likes,
                    }
                )
                review_id += 1  # Increment review ID
                review_content = ""  # Reset review content
                written_date = None  # Reset written date
                travel_type = None  # Reset travel type
                num_contributions = None  # Reset number of contributions
                personal_info = None  # Reset personal information
                likes = None  # Reset number of likes
            elif line.strip().endswith("• Family"):
                travel_type = "Family"
            elif line.strip().endswith("• Friends"):
                travel_type = "Friends"
            elif line.strip().endswith("• Couples"):
                travel_type = "Couples"
            elif line.strip().endswith("• Solo"):
                travel_type = "Solo"
            elif line.strip().endswith("contribution") or line.strip().endswith(
                "contributions"
            ):
                # Extract number of contributions
                match = re.search(r"(\d+)\s(contribution|contributions)", line)
                if match:
                    num_contributions = int(match.group(1))
            elif line.startswith("Written "):
                # Extract written date from the line
                match = re.search(r"Written (\w+ \d{1,2}, \d{4})", line)
                if match:
                    written_date_str = match.group(1)
                    # Parse written date into datetime object
                    written_date = datetime.strptime(
                        written_date_str, "%B %d, %Y"
                    ).strftime("%Y-%m-%d")
            elif line.strip().isdigit():
                # Extract number of likes
                likes = int(line.strip())
            elif "ConserveForests1" in line:
                # Start of reply detected, set in_reply flag to True
                in_reply = True
            elif (
                "This response is the subjective opinion of the management representative and not of Tripadvisor LLC."
                in line
            ):
                # End of reply detected, set in_reply flag to False
                in_reply = False
            elif not in_reply:
                # Check if line is before the number of contributions line and not part of a reply
                if num_contributions is None:
                    # Append line to personal information
                    if personal_info is None:
                        personal_info = line.strip()  # Initialize personal information
                    else:
                        personal_info += (
                            " " + line.strip()
                        )  # Append to existing personal information
                else:
                    # Append line to review content
                    review_content += line

        # Add the last review (if any) to the list
        if review_content.strip():
            reviews.append(
                {
                    "review_id": review_id,
                    "review_content": review_content.strip(),
                    "written_date": written_date,
                    "travel_type": travel_type,
                    "num_contributions": num_contributions,
                    "personal_info": personal_info,
                    "likes": likes,
                }
            )

    return reviews


def save_reviews_to_json(reviews, output_file):
    with open(output_file, "w") as file:
        json.dump(reviews, file, indent=4)


def export_review_to_txt(review):
    # Define the filename for the review
    filename = f"{review['review_id']}.txt"
    # Write review information to a text file
    with open(filename, "w") as file:
        file.write(f"{review['personal_info']}\n")
        # file.write(f"Review ID: {review['review_id']}\n")
        file.write(f"{review['review_content']}\n")
        file.write(f"{review['written_date']}\n")
        file.write(f"{review['travel_type']}\n")
        # file.write(f"{review['num_contributions']}\n")
        # file.write(f"{review['likes']}\n")


# Input file containing the reviews
input_file = "reviews.txt"
# Output file to save the extracted reviews as JSON
output_file = "extracted_reviews.json"

# Extract reviews from the input file
extracted_reviews = extract_reviews(input_file)

# Save extracted reviews to a JSON file
save_reviews_to_json(extracted_reviews, output_file)
print("Reviews extracted and saved to", output_file)


# Export each review information to a text file
for review in extracted_reviews:
    export_review_to_txt(review)
print("Individual review information exported to text files.")
