from tkinter import *
from functools import partial    # To prevent unwanted windows

import random

class Game:
    def __init__(self):

        # Formatting variables...
        self.game_stats_list = [50, 6]

        # In actual program this is blank and is populated with user calculations
        self.round_stats = ['silver ($4) | silver ($4) | lead ($0) - Cost: $10',
                                 'lead ($0) | silver ($4) | gold ($10) - Cost: $10',
                                 'lead ($0) | lead ($0) | copper ($2) - Cost: $10',
                                 'copper ($2) | lead ($0) | copper ($2) - Cost: $10',
                                 'lead ($0) | lead( $0) | lead ($0) - Cost: $10',
                                 'lead ($0) | lead ($0) | silver ($4) - Cost: $10',
                                 'silver ($4) | silver ($4) | silver ($4) - Cost: $10',
                                 'copper ($2) | silver ($4) | lead ($0) - Cost: $10',
                                 'lead ($0) | lead ($0) | copper ($2) - Cost: $10',
                                 'copper ($2) | copper ($2) | silver ($4) - Cost: $10',
                                 'copper ($2) | silver ($4) | silver ($4) - Cost: $10',
                                 'copper ($2) | lead ($0) | silver ($4) - Cost: $10']

        self.game_frame = Frame()
        self.game_frame.grid()

        # Heading Row
        self.heading_label = Label(self.game_frame, text="Play...",
                                   font="Arial 24 bold", padx=10,
                                   pady=10)
        self.heading_label.grid(row=0)

        # Instructions label
        self.stats_button = Button(self.game_frame, wrap=300, justify=LEFT,
                                        text="Game Stats",
                                        font="Arial 14", padx=10, pady=10,
                                        command=lambda: self.to_stats(self.round_stats, self.game_stats_list))
        self.stats_button.grid(row=1)

    def to_stats(self, game_history, game_stats):
        GameStats(self, game_history, game_stats)


class GameStats:
    def __init__(self, partner, game_history, game_stats):

        print(game_history)

        # Disable help button
        partner.stats_button.config(state=DISABLED)

        heading = "Arial 12 bold"
        content = "Arial 12"

        # Sets up child window (ie: help box)
        self.stats_box = Toplevel()

        # If users press cross at top, closes help and 'releases' help button

        self.stats_box.protocol('WM_DELETE_WINDOW', partial(self.close_stats, partner))

        # Set up GUI Frame
        self.stats_frame = Frame(self.stats_box)
        self.stats_frame.grid()

        # Set up Help heading (row 0)
        self.stats_heading_label = Label(self.stats_frame, text="Game Statistics",
                                         font="Arial 19 bold")
        self.stats_heading_label.grid(row=0)

        # To Export <instructions> (row 1)
        self.export_instructions = Label(self.stats_frame, text="Here are your Game Statistics."
                                                                "Please use the Export button to "
                                                                "access the results of each "
                                                                "round that you played", wrap=250,
                                                            font="Arial 10 italic",
                                                            justify=LEFT, fg="green",
                                                            padx=10, pady=10)
        self.export_instructions.grid(row=1)

        # Starting Balance (row 2)
        self.details_frame = Frame(self.stats_frame)
        self.details_frame.grid(row=2)

        # Starting balance (row 2.0)
        self.start_balance_label = Label(self.details_frame,
                                         text="Starting Balance:", font=heading,
                                         anchor="e")
        self.start_balance_label.grid(row=0, column=0, padx=0)

        self.start_balance_value_label = Label(self.details_frame, font=content,
                                               text="${}".format(game_stats[0]),
                                               anchor="w")
        self.start_balance_value_label.grid(row=0, column=1, padx=0)

        # Current Balance (row 2.2)
        self.current_balance_label = Label(self.details_frame,
                                           text="Current Balance:", font=heading,
                                           anchor="e")
        self.current_balance_label.grid(row=1, column=0, padx=0)

        self.current_balance_value_label = Label(self.details_frame, font=content,
                                                 text="${}".format(game_stats[0]),
                                                 anchor="w")
        self.current_balance_value_label.grid(row=0, column=1, padx=0)

        if game_stats[1] > game_stats[0]:
            win_loss = "Amount Won:"
            amount = game_stats[1] - game_stats[0]
            win_loss_fg = "green"
        else:
            win_loss = "Amount Lost:"
            amount = game_stats[0] - game_stats[1]
            win_loss_fg = "#660000"

        # Amount won / lost (row 2.3)
        self.wind_loss_label = Label(self.details_frame,
                                     text=win_loss, font=heading,
                                     anchor="e")
        self.wind_loss_label.grid(row=2, column=0, padx=0)

        self.wind_loss_value_label = Label(self.details_frame, font=content,
                                           text=len(game_history), anchor="w")
        self.wind_loss_value_label.grid(row=2, column=1, padx=0)

        # rounds played (row 2.4)

        self.export_dismiss_frame = Frame(self.stats_frame)
        self.export_dismiss_frame.grid(row=3)

        # Export Button
        self.export_button = Button(self.export_dismiss_frame, text="Export",
                                    font="Arial 12 bold",
                                    command=lambda: self.export(game_history))
        self.export_button.grid(row=0, column=0)

        # Dismiss button
        self.dismiss_button = Button(self.export_dismiss_frame, text="Dismiss",
                                     font="Arial 12 bold",
                                     command=partial(self.close_stats, partner))
        self.dismiss_button.grid(row=0, column=1)


    def close_stats(self, partner):
        # Put history button back to normal..
        partner.stats_button.config(state=NORMAL)
        self.stats_box.destroy()

    def export(self, game_history):
        print("you pushed export")

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("title goes here")
    something = Game()
    root.mainloop()