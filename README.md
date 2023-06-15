# Daily News Email

This Python script, `main.py`, fetches news articles from the News API and sends them via email using the `send_email` function from `send_email.py`. It retrieves news articles on various topics, such as Tesla, Apple, business news in the US, technology news from TechCrunch, and articles from The Wall Street Journal's website.

## Features

- Fetches news articles from the News API based on specific topics.
- Formats the news articles into an email message.
- Sends the email containing the news articles using the `send_email` function.
- The `send_email` function uses the Gmail SMTP server to send the email.

## Usage

1. Get your API key from [News API](https://newsapi.org/) by signing up for an account.
2. Replace `api_key` in `main.py` with your News API key.
3. Set up an email account to send the emails. You need a Gmail account for the script to work as it uses the Gmail SMTP server.
4. Replace `username` in `send_email.py` with your Gmail email address.
5. Set an environment variable named `PASSWORD` with the password for the Gmail account.
6. Run `main.py` using Python: `python main.py`.
7. The script will fetch the news articles, format them into an email, and send the email to the specified recipient (in this case, the same Gmail account).


## Email Configuration

To configure the email settings, make sure you have the following information:

- Gmail Account: You need a Gmail account to send the emails. If you don't have one, you can create a new account at [Gmail](https://www.gmail.com).
- App Password: Since the script uses the Gmail SMTP server, you need to generate an app password. Follow the steps below to generate an app password:
  1. Go to your [Google Account](https://myaccount.google.com/).
  2. Navigate to the "Security" section.
  3. Under the "Signing in to Google" section, select "App Passwords".
  4. Select the app you want to generate the password for (choose "Mail" if available).
  5. Follow the instructions to generate the app password.
  6. Copy the generated app password and set it as the value for the `PASSWORD` environment variable.

## Email Recipient

By default, the script sends the email to the same Gmail account used for authentication. If you want to send the email to a different recipient, modify the `receiver` variable in the `send_email.py` file. Replace the email address with the desired recipient's address.

## Running the Script

To run the script and send the daily news email:

1. Ensure you have installed the required dependencies by running `pip install -r requirements.txt` in your terminal or command prompt.
2. Set up the API key, email account, and recipient email as described above.
3. Execute the `main.py` script using Python: `python main.py`.
4. The script will fetch the latest news articles, format them into an email, and send the email to the specified recipient.
5. Check the recipient's email inbox to view the daily news email.

## Automation

To automate the execution of the script and receive the daily news email automatically, you can set up a cron job or task scheduler on your system. Configure the job to run the `main.py` script at the desired time intervals (e.g., daily, hourly) to fetch and send the latest news articles.

Remember to keep your API key, email account credentials, and app password secure. Do not share this sensitive information or commit it to a public code repository.

That's it! You now have a Python script that fetches news articles and sends a daily news email. Feel free to explore further enhancements, such as adding additional news sources or customizing the email template. Happy coding!
## Requirements

The project requires the following dependencies:

- requests==2.26.0

You can install the required dependencies by running `pip install -r requirements.txt`.

## Customization

You can customize the script by modifying the following:

- Topics: Modify the `topics` list in `main.py` to fetch news articles on different topics. You can find the available parameters for the News API in their [documentation](https://newsapi.org/docs/endpoints/everything).
- Email Content: Modify the email message format in `main.py` to customize how the news articles are displayed in the email.
- Email Subject: Modify the subject line of the email by changing the `Subject` field in `message` in `main.py`.
- Email Recipient: Change the `receiver` variable in `send_email.py` to specify the email address where you want to receive the news articles.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

## Acknowledgements

- [News API](https://newsapi.org/): An API that provides access to news articles from various sources worldwide.

Feel free to customize the above template to include specific details about your daily news email project, such as additional features, instructions, or any other relevant information.

