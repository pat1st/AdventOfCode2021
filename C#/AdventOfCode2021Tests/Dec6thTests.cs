using Microsoft.VisualStudio.TestTools.UnitTesting;
using AdventOfCode2021;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AdventOfCode2021.Tests
{
    [TestClass()]
    public class Dec6thTests
    {
        [TestMethod()]
        public void PredictSwarmSizeTest_inputSample_18days()
        {
            List<int> fishIn = new List<int> { 3, 4, 3, 1, 2 };
            int expectedCount = 26;
            int fishDays = 18;
            var advent = new Dec6th();
            int result = advent.PredictSwarmSize(fishIn, fishDays);
            Assert.AreEqual(expectedCount, result);
        }
        [TestMethod()]
        public void PredictSwarmSizeTest_inputSample_80days()
        {
            List<int> fishIn = new List<int> { 3, 4, 3, 1, 2 };
            int expectedCount = 5934;
            int fishDays = 80;
            var advent = new Dec6th();
            int result = advent.PredictSwarmSize(fishIn, fishDays);
            Assert.AreEqual(expectedCount, result);
        }
    }
}