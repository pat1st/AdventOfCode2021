using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AdventOfCode2021
{
    public class Dec1st
    {
        public int GetIncreaseCount(string measurements)
        {
            if (measurements.Trim().Length < 1)
            {
                return 0;
            }
            var splitted = measurements.Split(',');
            var counter = 0;
            var previous = -1;
            foreach (var item in splitted)
            {
                int actual = int.Parse(item);
                if (previous == -1)
                {
                    previous = actual;
                    continue;
                }
                if (actual > previous)
                {
                    counter++;
                }
                previous = actual;
            }

            return counter;
        }

        public int GetSlidingIncrease(string measurements)
        {
            if (measurements.Trim().Length < 6)
            {
                return 0;
            }
            var splitted = measurements.Split(',');
            if (splitted.Length < 4)
            {
                return 0;
            }
            var newMeasurements = "";

            for (int i = 0; i < splitted.Length - 2; i++)
            {
                var sum = int.Parse(splitted[i]) + int.Parse(splitted[i + 1]) + int.Parse(splitted[i + 2]);
                newMeasurements += sum.ToString() + ",";
            }

            return GetIncreaseCount(newMeasurements.Trim(','));
        }
    }
}
