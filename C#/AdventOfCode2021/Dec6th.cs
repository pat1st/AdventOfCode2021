using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AdventOfCode2021
{
    public class Dec6th
    {
        List<int> Fish;
        public Dec6th()
        {
            Fish = new List<int>();
        }

        public int PredictSwarmSize(List<int> fish, int days)
        {            
            for (int i = 0; i < days; i++)
            {
                for (int fishCounter = 0; fishCounter < fish.Count; fishCounter++)
                {
                    var actualFish = fish[fishCounter];
                    if (actualFish == 0)
                    {                        
                        fish[fishCounter] = 6;
                        fish.Add(9);
                    }
                    else
                    {
                        fish[fishCounter]--;
                    }
                }
                //Console.WriteLine(string.Join(",", fish));
            }
            return fish.Count;
        }
    }
}
