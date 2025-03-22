# YouTube Trending Video Titles Generator

This project fetches trending video titles from YouTube, extracts keywords from those titles, and generates new video titles using predefined templates.

## Features

- Fetch trending video titles from YouTube
- Exclude music videos from the fetched titles
- Extract keywords from the trending titles
- Generate new video titles using predefined templates

## Requirements

- Python 3.x
- `numpy`
- `google-api-python-client`
- `scikit-learn`

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/aliihjt/Youtube-Helper
    cd Youtube-Helper
    ```

2. Install the required dependencies:

    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Replace `YOUR_API_KEY` in [main.py] with your YouTube Data API key.

2. Run the script:

    ```sh
    python main.py
    ```

## Example

```sh
Trending Titles: ['Canada vs. Mexico: Extended Highlights | CONCACAF Nations League Semi-Final | CBS Sports Golazo']
Generated Video Titles: ['Why Mexico is Changing Everything!']
