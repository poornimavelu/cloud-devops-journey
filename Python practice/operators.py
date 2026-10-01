beat_colour_options=2;
pattern_slots=5;
iced_latte_price=4.75;
total_cupcakes=27;
box_capacity=6;
print("Total unique bracelet combinations:", beat_colour_options ** pattern_slots, type(beat_colour_options))
print("Full gift boxes filled:", total_cupcakes//box_capacity, type(box_capacity))
print("Cupcakes left over for you:",total_cupcakes%box_capacity, type(box_capacity))
print("Coffee budget:",iced_latte_price*15, type(iced_latte_price))

