#include <gtest/gtest.h>
#include "demo.h"

class DemoTests : public ::testing::Test
{
protected:
	// You can remove any or all of the following functions if their bodies would
	// be empty.

	DemoTests()
	{
		// You can do set-up work for each test here.
	}

	~DemoTests() override
	{
		// You can do clean-up work that doesn't throw exceptions here.
	}

	// If the constructor and destructor are not enough for setting up
	// and cleaning up each test, you can define the following methods:

	void SetUp() override
	{
		// Code here will be called immediately after the constructor (right
		// before each test).
	}

	void TearDown() override
	{
		// Code here will be called immediately after each test (right
		// before the destructor).
	}

	// Class members declared here can be used by all tests in the test suite
	// for Foo.
};

TEST(DemoTests, test_add)
{
	EXPECT_EQ(7, demo_add(3, 4));
}

TEST(DemoTests, test_sub)
{
	EXPECT_EQ(-1, demo_sub(3, 4));
}

TEST(DemoTests, test_mul)
{
	EXPECT_EQ(12, demo_mul(3, 4));
}

TEST(DemoTests, test_div)
{
	EXPECT_EQ(0, demo_div(3, 4));
}
