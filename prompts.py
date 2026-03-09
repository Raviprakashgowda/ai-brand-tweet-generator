def brand_analysis_prompt(brand, industry, product, objective):

    return f"""
You are a social media strategist.

Analyze the brand based on the following details.

Brand Name: {brand}
Industry: {industry}
Product: {product}
Campaign Objective: {objective}

Identify:
1. Brand tone
2. Target audience
3. Communication style
4. Content themes

Return the answer in bullet points.
"""


def tweet_generation_prompt(brand, voice):

    return f"""
You are a social media manager for {brand}.

Brand Voice:
{voice}

Generate 10 tweets that match this voice.

Requirements:
- Mix of engaging, witty, promotional and informative tweets
- Under 280 characters
- Include hashtags where appropriate
- Make tweets sound natural and human
"""