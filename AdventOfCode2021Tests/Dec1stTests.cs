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
    public class Dec1stTests
    {
        [TestMethod()]
        public void GetIncreaseCountTest_EmptyString_Returns_0()
        {
            Dec1st dec1st = new Dec1st();
            var result = dec1st.GetIncreaseCount("");
            var expected = 0;
            Assert.AreEqual(expected, result);
        }

        [TestMethod()]
        public void GetIncreaseCountTest_SingleValue_Returns_0()
        {
            Dec1st dec1st = new Dec1st();
            var result = dec1st.GetIncreaseCount("125");
            var expected = 0;
            Assert.AreEqual(expected, result);
        }
        [TestMethod()]
        public void GetIncreaseCountTest_TwoValuesSecondHigher_Returns_1()
        {
            Dec1st dec1st = new Dec1st();
            var result = dec1st.GetIncreaseCount("125, 126");
            var expected = 1;
            Assert.AreEqual(expected, result);
        }
        [TestMethod()]
        public void GetIncreaseCountTest_TwoValuesSecondLower_Returns_0()
        {
            Dec1st dec1st = new Dec1st();
            var result = dec1st.GetIncreaseCount("125, 124");
            var expected = 0;
            Assert.AreEqual(expected, result);
        }
        [TestMethod()]
        public void GetIncreaseCountTest_SampleOfPuzzle_Returns_7()
        {
            Dec1st dec1st = new Dec1st();
            var result = dec1st.GetIncreaseCount("199, 200, 208, 210, 200, 207, 240, 269, 260, 263");
            var expected = 7;
            Assert.AreEqual(expected, result);
        }

        [TestMethod()]
        public void GetSlidingIncreaseTest_TwoValuesOnly_Returns_0()
        {
            Dec1st dec1st = new Dec1st();
            var result = dec1st.GetSlidingIncrease("199, 200");
            var expected = 0;
            Assert.AreEqual(expected, result);
        }
        [TestMethod()]
        public void GetSlidingIncreaseTest_FourIncreasingValues_Returns_1()
        {
            Dec1st dec1st = new Dec1st();
            var result = dec1st.GetSlidingIncrease("1,2,3,4");
            var expected = 1;
            Assert.AreEqual(expected, result);
        }
    }
}