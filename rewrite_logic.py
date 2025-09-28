def rewrite_query(original_query, rewrite_type, location=None, interests=None, device=None, user_profile=None):
    """
    Rewrites a user query based on selected rewrite strategy and personalization fields.
    Parameters:
        original_query (str): The initial user query.
        rewrite_type (str): Strategy to apply (e.g., 'simplification', 'elaboration', 'formalization', 'localization').
        location (str, optional): User's location for contextual relevance.
        interests (str, optional): User interests to guide elaboration.
        device (str, optional): Device type for optimization hints.
        user_profile (str, optional): Behavioral or demographic profile for tailoring.
    Returns:
        str: A rewritten query that reflects the selected strategy and personalization.
    """
    rewrite = original_query
    # Simplification
    if "simplification" in rewrite_type:
        rewrite = f"Explain in simple terms: {rewrite}"
    # Elaboration
    if "elaboration" in rewrite_type:
        interest_context = f" considering {interests}" if interests else ""
        rewrite = f"Provide a detailed explanation of: {rewrite}{interest_context}"
    # Localization
    if "localization" in rewrite_type and location:
        rewrite = f"{rewrite} relevant to {location}"
    # Formalization
    if "formalization" in rewrite_type:
        rewrite = f"Formally describe: {rewrite}"
    # Device/User Profile (optional personalization)
    if device:
        rewrite += f" (optimized for {device})"
    if user_profile:
        rewrite += f" [tailored for {user_profile}]"
    return rewrite