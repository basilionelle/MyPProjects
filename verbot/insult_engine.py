"""
InsultEngine - Core logic for generating verbal content
"""
import json
import random
import os
from pathlib import Path

class InsultEngine:
    def __init__(self):
        self.intensity = "light"
        self.data_dir = Path(__file__).parent / "data"
        self.load_data()
    
    def load_data(self):
        """Load insult templates from JSON files"""
        self.templates = {}
        for level in ["light", "medium", "brutal"]:
            file_path = self.data_dir / f"{level}.json"
            if file_path.exists():
                with open(file_path) as f:
                    self.templates[level] = json.load(f)
            else:
                self.templates[level] = self._get_default_templates(level)
                # Save default templates
                with open(file_path, "w") as f:
                    json.dump(self.templates[level], f, indent=2)
    
    def _get_default_templates(self, level):
        """Get default templates if JSON files don't exist"""
        defaults = {
            "light": {
                "appearance": [
                    "You look like a failed science experiment.",
                    "Even Photoshop gave up on you."
                ],
                "intelligence": [
                    "Your brain is a ghost town.",
                    "You make rocks look smart."
                ],
                "personality": [
                    "You're about as useful as a screen door on a submarine.",
                    "Your personality is like a dial-up modem: slow and irritating."
                ]
            },
            "medium": {
                "appearance": [
                    "You look like something I drew with my left hand.",
                    "Did your face catch on fire and someone tried to put it out with a fork?"
                ],
                "intelligence": [
                    "Your IQ is lower than your shoe size.",
                    "You're the reason we have warning labels on shampoo."
                ],
                "personality": [
                    "You have the charm of a brick wall and half the personality.",
                    "You're the human equivalent of a participation award."
                ]
            },
            "brutal": {
                "appearance": [
                    "You look like you fell out of the ugly tree and hit every branch on the way down.",
                    "Your face looks like it was on fire and someone tried to put it out with a chainsaw."
                ],
                "intelligence": [
                    "You're so dense, light bends around you.",
                    "If brains were dynamite, you wouldn't have enough to blow your nose."
                ],
                "personality": [
                    "You have the personality of a wet paper bag filled with disappointment.",
                    "You're the reason aliens haven't visited Earth."
                ]
            }
        }
        return defaults[level]
    
    def set_intensity_level(self, level):
        """Set the intensity level for generated content"""
        if level in ["light", "medium", "brutal"]:
            self.intensity = level
    
    def generate_random_insult(self, category=None):
        """Generate a random insult from the current intensity level"""
        templates = self.templates[self.intensity]
        if category and category in templates:
            return random.choice(templates[category])
        categories = list(templates.keys())
        random_category = random.choice(categories)
        return random.choice(templates[random_category])
    
    def generate_keyword_insult(self, target, category=None):
        """Generate an insult targeting a specific name/keyword"""
        insult = self.generate_random_insult(category)
        if not target:
            return insult
        
        # Add the target name to personalize the insult
        if "you" in insult.lower():
            return insult.replace("you", target)
        elif "your" in insult.lower():
            return insult.replace("Your", f"{target}'s")
        else:
            return f"{target}, {insult}"
