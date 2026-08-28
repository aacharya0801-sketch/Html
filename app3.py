# TASK 1 - generate_chamber
def generate_chamber(idx: int, history: list) -> dict:
    name = CHAMBER_NAMES[idx % len(CHAMBER_NAMES)]
    hist = " | ".join(history[-3:]) if history else "None"
    text = call_groq( "Write immersive fantasy-mystery chamber descriptioms. Output JSON: title, description, clue.", f"Chamber {idx+1}. Title: {name}. History: {hist}. Return valid JSON only.", 1.0)
    if text:
        try:
            d = json.loads(text)
        if all(k in d for k in ["title","description","clue"]): return d except Exception: pass
    clues = ["A cracked clock face points toward a hidden seam in the wall.","A blue crystal hums whenever the truth is spoken nearby.", "Dust shifts in a pattern that looks almost like writing.", "A silent spark jumps between metal rings above the doorway."]
    return("title": name, "description": f"{name} opens before you like a forgotten dream. Pale light spills across ancient stone.", "clue": clues{idx % len(clues)})
# TASK 2 - generate_relic
def generate_relic(chamber_title: str, description: str, count: int) -> dict:
    text = call.groq("Create magical relics for a vault adventure. Output JSON: name, rarity, lore, power, art_prompt. Rarity: Common/Rare/Epic/Legendary.", f"Relic from: {chamber_title}\n{description}\nRelics so far: {count}\nReturn valid JSON only.", 1.0)
    if text:
        try:
            d = json.loads(text)
            if all(k in d for k in ["name","rarity","lore","power","art_prompt"]):
return d
        except Exception: pass
    d = RELIC_FALBBACKS[count % len(RELIC_FALLBACKS)].copy()
    d["lore"] += f" it resonates with the memory of {chambar_title}."
    return d
def genrate_final_ending(player_name: str, relic_names: list, chambar_history:list -> str: text = call_groq("Narrate the final ending of a mystery vault game. Triumphant, magical, under 160 words.", f"Player: {player_name}\nRelics: {', '.join(relic_names) or 'None'}\nChambers: {', '.join(chamber_history) or 'None'}")
                         return text or (f"The final seal withdraws as {player_name or 'Traveler'} steps forward, carrying " f"{', '/join(relic names) or 'no relics'}. Ancient light spills across the floor." f"A voice older than stone declares: Vault Access Granted. Your journey is now legend.")

                    def apply_scenario(sc: dict):
                        s = st.session_state

                        ch = maybe_generate_current_chamber()
                        if not ch: return

                        change_trust(sc["trust"]); s.streak += 1
                        append_log("YOU", sc["message"])
                        append_log("SENTINEL", ask_sentinel(s.player_name or "Traveler", sc["message"],s.trust_score, s.sentinel_mood))