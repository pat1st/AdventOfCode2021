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
        static int maxCount = 200000;

        public int PredictSwarmSize(List<int> fish, int days)
        {
            List<List<int>> fishTanks = distributeFishToTanks(fish);

            
            bool reDistribution = false;

            for (int i = 0; i < days; i++)
            {
                foreach (var fishTank in fishTanks)
                {
                    for (int fishCounter = 0; fishCounter < fishTank.Count; fishCounter++)
                    {
                        fishMakeFishies(fishTank, fishCounter);
                    }
                    if (fishTank.Count > maxCount)
                    {
                        reDistribution = true;
                    }
                    Console.Write(fishTank.Count + " ");
                }
                
                if (reDistribution)
                {
                    Console.WriteLine("redist..");
                    List<List<int>> SubFishTanks = distributeFishToTanks(fish);
                    foreach (var item in fishTanks)
                    {
                        SubFishTanks.AddRange(distributeFishToTanks(item));
                    }
                    fishTanks = SubFishTanks;
                    reDistribution = false;
                }

                Console.WriteLine(i.ToString() + ": ----------" + Environment.NewLine); // + fishTanks[0].Count + " " + fishTanks[1].Count);
                Console.WriteLine(countFishTotal(fishTanks));

            }
            return int.Parse(countFishTotal(fishTanks));
        }

        private static List<List<int>> distributeFishToTanks(List<int> fish)
        {
            var fishTanks = new List<List<int>>(maxCount);
            foreach (var singleFish in fish)
            {
                fishTanks.Add(new List<int> { singleFish });
            }

            return fishTanks;
        }

        private string countFishTotal(List<List<int>> fishTanks)
        {
            int i = 0;
            foreach (var item in fishTanks)
            {
                i += item.Count;
            }
            return i.ToString();
        }

        private static void fishMakeFishies(List<int> fish, int fishCounter)
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
    }
}
