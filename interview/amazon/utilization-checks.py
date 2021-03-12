# Utilization Checks

# https://aonecode.com/amazon-online-assessment-utilization-checks

import math

class UtilizationChecks:

    def solve(self, instances, averageUtil):
        i = 0
        while i < len(averageUtil):
            if 25 <= averageUtil[i] <= 60:
                i += 1
                continue
            
            # we need increase or decrease #. of instances
            if averageUtil[i] > 60:
                if 2 * instances > 2 * pow(10, 8):
                    continue
                
                instances *= 2

            else:
                if instances == 1:
                    i += 1
                    continue
                
                instances = math.ceil(instances / 2)


            i += 10

        print(instances)
        return instances


uc = UtilizationChecks()
uc.solve(2, [25, 23, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 76, 80])
uc.solve(3, [5, 10, 80])
uc.solve(5, [30, 5, 4, 8, 19, 89])
