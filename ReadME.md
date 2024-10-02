
---

![consumelogo.jpg](Resources%2Fconsumelogo.jpg)

# ConsumeWise - Health & Product Analysis Whatsapp Bot

### Tagline : Instant Health Insights, Just A Text Away!

**ConsumeWise** is a WhatsApp bot designed to help users analyze food products based on their specific health needs. Users can create personalized health profiles (e.g., allergies, diabetes), search for products by barcode, and receive comprehensive health analyses, including allergy alerts, nutritional insights, food processing levels, and misleading claim detection. Additionally, the bot offers better food recommendations based on health profiles, guiding users toward healthier choices.

---

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Prerequisites](#prerequisites)
- [Architecture Diagram](#architecture-diagram)
- [Setup Video](#setup-video) 
- [Project Setup](#project-setup)
  - [1. Clone the Repository](#1-clone-the-repository)
  - [2. Set Up a Virtual Environment in PyCharm](#2-set-up-a-virtual-environment-in-pycharm)
  - [3. Install Flask and Dependencies](#3-install-flask-and-dependencies)
  - [4. Set Up Twilio WhatsApp](#4-set-up-twilio-whatsapp)
    - [Creating a Twilio Account](#creating-a-twilio-account)
    - [Setting Up the WhatsApp Sandbox](#setting-up-the-whatsapp-sandbox)
  - [5. Run Ngrok](#5-run-ngrok)
    - [Creating a Ngrok Account](#creating-a-ngrok-account)
  - [6. Run the Flask Application](#6-run-the-flask-application)
  - [7. Interact with the Bot](#7-interact-with-the-bot)
- [Working of the Bot](#working-of-the-bot)
- [Usage](#usage)
- [Detailed Twilio Setup](#detailed-twilio-setup)
- [Ngrok Setup](#ngrok-setup)
- [Flask Route Explanation](#flask-route-explanation)
- [Requirements](#requirements)
- [Troubleshooting](#troubleshooting)
- [Future Improvements](#future-improvements)
- [License](#license)

---

## Features

- **Health Profile Creation**: Users can input health conditions (e.g., diabetes or allergies) to generate a personalized profile.
- **Product Search by Barcode**: Users can search for a product using its barcode.
- **Allergy Alerts**: Detects potential allergens in products based on the user’s profile.
- **Nutritional Analysis**: Assesses products for suitability based on the user's health conditions.
- **Claim Verification**: Detects whether claims like "natural" or "sugar-free" are misleading, based on ingredient analysis.

---

## Technologies Used

- **PyCharm**: Python IDE for development.
- **Twilio API**: For enabling WhatsApp messaging.
- **Ngrok**: Exposes the local server to the internet, allowing Twilio to communicate with the bot.
- **Python (Flask)**: For backend development.

---

## Prerequisites

Before you start, ensure you have the following:

- **PyCharm** installed on your machine.
- **Python 3.x** installed.
- A **Twilio account** with access to the WhatsApp Sandbox.
- A **Ngrok account** for exposing your local Flask server to the internet.

---

## Architecture Diagram

![Flowchart of GENAI Final.drawio.png](Resources%2FFlowchart%20of%20GENAI%20Final.drawio.png)

---

## Setup Video

[Setup Video.mp4](Resources%2FSetup%20Video.mp4)

---
## Project Setup

### 1. Clone the Repository

Start by cloning the project repository to your local machine:

```bash
git clone https://github.com/your-repo/ConsumeWise.git
```

Once cloned, open the project in **PyCharm**:

- Open PyCharm, go to **File** > **Open**, and select the cloned project folder.

---

### 2. Set Up a Virtual Environment in PyCharm

1. In PyCharm, go to **File** > **Settings** > **Project: <Your Project Name>** > **Python Interpreter**.
2. Click the gear icon, then select **Add**.
3. Choose **New environment** and select **Virtualenv**.
4. Confirm the creation of the virtual environment by clicking **OK**.

---

### 3. Install Flask and Dependencies

Once the virtual environment is set up, install the required dependencies using the `requirements.txt` file.

1. Open the terminal in PyCharm.
2. Run the following command:

```bash
pip install -r requirements.txt
```

This will install the necessary Python packages: Flask, Twilio, requests, and Ngrok.

---

### 4. Set Up Twilio WhatsApp

#### Creating a Twilio Account

1. **Sign Up**: Go to [Twilio](https://www.twilio.com/) and click on **Sign up**.
2. **Fill in Details**: Provide the required information (name, email, password).
3. **Email Verification**: Verify your email address.
4. **Account Setup**: Follow the prompts to complete the account setup process.

#### Setting Up the WhatsApp Sandbox

1. **Access the Twilio Console**: Once signed in, navigate to the **Twilio Console**.
2. **Navigate to WhatsApp**:
   - In the left sidebar, click on **Messaging** > **Try It Out** > **WhatsApp Sandbox**.
3. **Join the Sandbox**:
   - Twilio will provide a WhatsApp-enabled number and a **join code**.
   - Add the Twilio number to your WhatsApp contacts.
   - Send a WhatsApp message to that number with the following format:
     ```text
     join your-join-code
     ```

4. **Configure the Twilio Webhook**:
   - In the **WhatsApp Sandbox Settings**, under the **WHEN A MESSAGE COMES IN** field, you will paste the Ngrok forwarding URL (to be done later).

---

### 5. Run Ngrok

Ngrok allows you to expose your local Flask application to the internet.

#### Creating a Ngrok Account

1. **Sign Up**: Go to [Ngrok](https://ngrok.com/) and click on **Sign up**.
2. **Fill in Details**: Provide the required information (name, email, password).
3. **Download Ngrok**: After signing up, download Ngrok from [Ngrok's website](https://ngrok.com/download).
4. **Install Ngrok**: Extract the downloaded file and place it in a convenient directory.

#### Step 1: Start Ngrok

1. Open a terminal and run the following command to expose your Flask app running on `localhost:5000` to the internet:

   ```bash
   ngrok http 5000
   ```

   Ngrok will provide a forwarding URL that looks like this:

   ```text
   http://abcd1234.ngrok.io
   ```

#### Step 2: Complete Twilio Webhook Setup

1. Copy the **Ngrok forwarding URL** from the terminal.
2. Go back to the **Twilio Console** > **WhatsApp Sandbox Settings**.
3. Paste the Ngrok forwarding URL in the **WHEN A MESSAGE COMES IN** field, appending `/whatsapp` at the end:

   ```text
   http://abcd1234.ngrok.io/whatsapp
   ```

---

### 6. Run the Flask Application

To start the Flask application, follow these steps:

1. Open the terminal in PyCharm.
2. Run the Flask app by executing the following command:

   ```bash
   python main.py
   ```

This will start the Flask server at `http://127.0.0.1:5000`.

---

### 7. Interact with the Bot

With everything set up, you can now interact with the bot:

1. Open WhatsApp and send a message (e.g., "Hello") to the Twilio number.
2. The bot will respond with a welcome message and guide you through creating a health profile or searching for a product.

---

## Working of the Bot

The bot functions through a combination of Flask webhooks and Twilio’s messaging service for WhatsApp. Here's how the interaction works:

1. **User Sends a Message**:
   - When a user sends a message to the WhatsApp bot (via Twilio), the message is forwarded to the Flask server through the webhook endpoint `/whatsapp`.

2. **Flask Processes the Message**:
   - The bot identifies the message type (text or command) and triggers appropriate responses.
   - Example: When the user sends "Hello," the bot recognizes it as an initiation and responds with a greeting.

3. **Health Profile Setup**:
   - The bot asks for the user’s health information such as diabetes or allergies.
   - The user's responses are stored in memory (or a database), and the bot uses this information to personalize future recommendations.

4. **Product Search**:
   - When a user submits a product’s barcode, the bot queries a database or external API (like Open Food Facts) to fetch details about the product.
   - The bot compares the product’s ingredients and nutritional information against the user’s health profile to check for potential allergens or health risks.

5. **Allergy Alerts & Nutritional Warnings**:
   - If the product contains allergens that the user has mentioned, the bot issues an allergy alert.
   - Similarly, the bot provides nutritional warnings based on the user’s health profile, such as flagging high sugar levels for diabetic users.

6. **Claim Verification**:
   - The bot can analyze claims like “sugar-free” or “natural” by looking up the product’s ingredients and verifying whether the claim is accurate or misleading.

7. **Bot Response**:
   - The bot generates a response message with the analysis results and sends it back to the user via WhatsApp.

---

## Usage

1. **Create a Health Profile**:
   - Provide information about your health conditions.
   - Example:
     ```text
     Do you have diabetes? (yes/no): yes
     Do you have any allergies? (yes/no): yes
     Enter any allergies you have: peanuts, milk
     ```

2. **Search for Products by Barcode**:
   - Enter a product’s barcode to get detailed health-related information.
   - Example:
     ```text
     Enter the product barcode: 8906009501017
     ```

3. **Check Misleading Claims**:
   - Provide the product barcode and a claim (e.g., "sugar-free") to check its validity.
   - Example:
     ```text
     Enter the claim to analyze: sugar-free
     ```
     
---

## Detailed Twilio Setup

1. **Sign Up for Twilio**: Go to [Twilio](https://www.twilio.com/) and create an account.
2. **Configure WhatsApp Sandbox**:
   - Go to **Messaging** > **Try It Out** > **WhatsApp Sandbox**.
   - Add the provided WhatsApp-enabled number and send the **join code** via WhatsApp.
3. **Set the Webhook**: Once you have the Ngrok URL, paste it into the **WHEN A MESSAGE COMES IN** field in the **WhatsApp Sandbox Settings**, appending `/whatsapp`.

---

## Ngrok Setup

1. **Install Ngrok**: Download it from [Ngrok’s website](https://ngrok.com/download) and extract it.
2. **Expose Flask on Port 5000**: Run the following command to expose your Flask app:
   ```bash
   ngrok http 5000
   ```
3. In **Resources** folder there is a [ngrok.exe](Resources/ngrok.exe) file present for system installation of ngrok.  

---

## Flask Route Explanation

In the `main.py` file, the Flask application defines the following routes:

- **/whatsapp**: Receives incoming messages from WhatsApp and processes them.
- **/health**:

 Handles user health profile creation.
- **/product-search**: Manages product lookup by barcode.

---

## Requirements

- Flask
- Twilio
- Requests
- Ngrok

The required packages for this project are listed in the `requirements.txt` file. Install them using:

```bash
pip install -r requirements.txt
```

---

## Troubleshooting

If you encounter issues:

- **Twilio Webhook**: Ensure that the Ngrok URL is correctly set in the Twilio Console.
- **Ngrok**: Check that Ngrok is running and forwarding requests to `localhost:5000`.
- **Flask App**: Make sure the Flask application is running without errors.

---

## Future Improvements

- **Multi-language Support**: Adding support for more languages to reach a wider audience.
- **Product Database Expansion**: Integrating with multiple food databases for a more comprehensive product analysis.

---

## License

This project is licensed under the MIT License.

---
