class CompoundInterest:
    def compound(self, principal, interest, time):
        self.principal = principal
        self.interest = interest
        self.time = time
        times_per_year = 12
        total = principal * pow((1 + interest/times_per_year), 12 * time)


# A = P(1 + r/n)^nt
# A = P(1 + r/12)^12t