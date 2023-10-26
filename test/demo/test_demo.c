#include <gtest/gtest.h>
#include "demo.h"

TEST(demo, test_demo) {
  // Expect equality.
  EXPECT_EQ( 7, add(3, 4));
}
