from app.models.baseModel import BaseModel
from app.models.user import User
from app.models.place import Place

class Review(BaseModel):
    def __init__(self, text, rating, place, user):
        super().__init__()
        # Validate text
        if text:
            self.text = text
        else:
            raise ValueError("text content is required")

        # Validate rating between 1 and 5
        if 1 <= rating <= 5:
            self.rating = rating
        else:
            raise ValueError("rating must be between 1 and 5")

        # Check if user is valid and exists
        if isinstance(user, User) and self.user_exists(user):
            self.user = user
        else:
            raise ValueError("invalid user")

        # Check if place is valid and exists
        if isinstance(place, Place) and self.place_exists(place):
            self.place = place
        else:
            raise ValueError("invalid place")

        # Link the review to the user and place
        ##user.add_review(self)
        ##place.add_review(self)

    @staticmethod
    def user_exists(user):
        """Check if the user exists in the database."""
        # Replace with actual logic to check if the user is in the database
        return True

    @staticmethod
    def place_exists(place):
        """Check if the place exists in the database."""
        # Replace with actual logic to check if the place is in the database
        return True
