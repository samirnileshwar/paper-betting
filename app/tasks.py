from celery import shared_task
from celery.utils.log import get_task_logger


logger = get_task_logger(__name__)
def _getObject():
    return [
    {
        "id": "4ca2f33559d32db74f8e8894a71312b5",
        "sport_key": "basketball_nba",
        "sport_title": "NBA",
        "commence_time": "2024-02-24T00:40:00Z",
        "home_team": "Atlanta Hawks",
        "away_team": "Toronto Raptors",
        "bookmakers": [
            {
                "key": "draftkings",
                "title": "DraftKings",
                "last_update": "2024-02-23T13:40:35Z",
                "markets": [
                    {
                        "key": "h2h",
                        "last_update": "2024-02-23T13:40:35Z",
                        "outcomes": [
                            {
                                "name": "Atlanta Hawks",
                                "price": 1.37
                            },
                            {
                                "name": "Toronto Raptors",
                                "price": 3.2
                            }
                        ]
                    },
                    {
                        "key": "spreads",
                        "last_update": "2024-02-23T13:40:35Z",
                        "outcomes": [
                            {
                                "name": "Atlanta Hawks",
                                "price": 1.91,
                                "point": -7.0
                            },
                            {
                                "name": "Toronto Raptors",
                                "price": 1.91,
                                "point": 7.0
                            }
                        ]
                    },
                    {
                        "key": "totals",
                        "last_update": "2024-02-23T13:40:35Z",
                        "outcomes": [
                            {
                                "name": "Over",
                                "price": 1.87,
                                "point": 245.0
                            },
                            {
                                "name": "Under",
                                "price": 1.95,
                                "point": 245.0
                            }
                        ]
                    }
                ]
            },
            {
                "key": "lowvig",
                "title": "LowVig.ag",
                "last_update": "2024-02-23T13:41:04Z",
                "markets": [
                    {
                        "key": "h2h",
                        "last_update": "2024-02-23T13:41:04Z",
                        "outcomes": [
                            {
                                "name": "Atlanta Hawks",
                                "price": 1.36
                            },
                            {
                                "name": "Toronto Raptors",
                                "price": 3.3
                            }
                        ]
                    },
                    {
                        "key": "spreads",
                        "last_update": "2024-02-23T13:41:04Z",
                        "outcomes": [
                            {
                                "name": "Atlanta Hawks",
                                "price": 1.94,
                                "point": -7.0
                            },
                            {
                                "name": "Toronto Raptors",
                                "price": 1.94,
                                "point": 7.0
                            }
                        ]
                    },
                    {
                        "key": "totals",
                        "last_update": "2024-02-23T13:41:04Z",
                        "outcomes": [
                            {
                                "name": "Over",
                                "price": 1.94,
                                "point": 245.5
                            },
                            {
                                "name": "Under",
                                "price": 1.94,
                                "point": 245.5
                            }
                        ]
                    }
                ]
            },
            {
                "key": "betonlineag",
                "title": "BetOnline.ag",
                "last_update": "2024-02-23T13:40:35Z",
                "markets": [
                    {
                        "key": "h2h",
                        "last_update": "2024-02-23T13:40:35Z",
                        "outcomes": [
                            {
                                "name": "Atlanta Hawks",
                                "price": 1.36
                            },
                            {
                                "name": "Toronto Raptors",
                                "price": 3.3
                            }
                        ]
                    },
                    {
                        "key": "spreads",
                        "last_update": "2024-02-23T13:40:35Z",
                        "outcomes": [
                            {
                                "name": "Atlanta Hawks",
                                "price": 1.91,
                                "point": -7.0
                            },
                            {
                                "name": "Toronto Raptors",
                                "price": 1.91,
                                "point": 7.0
                            }
                        ]
                    },
                    {
                        "key": "totals",
                        "last_update": "2024-02-23T13:40:35Z",
                        "outcomes": [
                            {
                                "name": "Over",
                                "price": 1.87,
                                "point": 245.0
                            },
                            {
                                "name": "Under",
                                "price": 1.95,
                                "point": 245.0
                            }
                        ]
                    }
                ]
            },
            {
                "key": "pointsbetus",
                "title": "PointsBet (US)",
                "last_update": "2024-02-23T13:40:35Z",
                "markets": [
                    {
                        "key": "h2h",
                        "last_update": "2024-02-23T13:40:35Z",
                        "outcomes": [
                            {
                                "name": "Atlanta Hawks",
                                "price": 1.34
                            },
                            {
                                "name": "Toronto Raptors",
                                "price": 3.3
                            }
                        ]
                    },
                    {
                        "key": "spreads",
                        "last_update": "2024-02-23T13:40:35Z",
                        "outcomes": [
                            {
                                "name": "Atlanta Hawks",
                                "price": 1.91,
                                "point": -7.0
                            },
                            {
                                "name": "Toronto Raptors",
                                "price": 1.91,
                                "point": 7.0
                            }
                        ]
                    },
                    {
                        "key": "totals",
                        "last_update": "2024-02-23T13:40:35Z",
                        "outcomes": [
                            {
                                "name": "Over",
                                "price": 1.91,
                                "point": 245.5
                            },
                            {
                                "name": "Under",
                                "price": 1.91,
                                "point": 245.5
                            }
                        ]
                    }
                ]
            },
            {
                "key": "williamhill_us",
                "title": "Caesars",
                "last_update": "2024-02-23T13:38:20Z",
                "markets": [
                    {
                        "key": "h2h",
                        "last_update": "2024-02-23T13:38:20Z",
                        "outcomes": [
                            {
                                "name": "Atlanta Hawks",
                                "price": 1.36
                            },
                            {
                                "name": "Toronto Raptors",
                                "price": 3.22
                            }
                        ]
                    },
                    {
                        "key": "spreads",
                        "last_update": "2024-02-23T13:38:20Z",
                        "outcomes": [
                            {
                                "name": "Atlanta Hawks",
                                "price": 1.91,
                                "point": -7.0
                            },
                            {
                                "name": "Toronto Raptors",
                                "price": 1.91,
                                "point": 7.0
                            }
                        ]
                    },
                    {
                        "key": "totals",
                        "last_update": "2024-02-23T13:38:20Z",
                        "outcomes": [
                            {
                                "name": "Over",
                                "price": 1.87,
                                "point": 245.0
                            },
                            {
                                "name": "Under",
                                "price": 1.95,
                                "point": 245.0
                            }
                        ]
                    }
                ]
            },
            {
                "key": "wynnbet",
                "title": "WynnBET",
                "last_update": "2024-02-23T13:41:03Z",
                "markets": [
                    {
                        "key": "h2h",
                        "last_update": "2024-02-23T13:41:03Z",
                        "outcomes": [
                            {
                                "name": "Atlanta Hawks",
                                "price": 1.37
                            },
                            {
                                "name": "Toronto Raptors",
                                "price": 3.25
                            }
                        ]
                    },
                    {
                        "key": "spreads",
                        "last_update": "2024-02-23T13:41:03Z",
                        "outcomes": [
                            {
                                "name": "Atlanta Hawks",
                                "price": 1.91,
                                "point": -7.0
                            },
                            {
                                "name": "Toronto Raptors",
                                "price": 1.91,
                                "point": 7.0
                            }
                        ]
                    },
                    {
                        "key": "totals",
                        "last_update": "2024-02-23T13:41:03Z",
                        "outcomes": [
                            {
                                "name": "Over",
                                "price": 1.91,
                                "point": 245.0
                            },
                            {
                                "name": "Under",
                                "price": 1.91,
                                "point": 245.0
                            }
                        ]
                    }
                ]
            },
            {
                "key": "mybookieag",
                "title": "MyBookie.ag",
                "last_update": "2024-02-23T13:40:35Z",
                "markets": [
                    {
                        "key": "h2h",
                        "last_update": "2024-02-23T13:40:35Z",
                        "outcomes": [
                            {
                                "name": "Atlanta Hawks",
                                "price": 1.36
                            },
                            {
                                "name": "Toronto Raptors",
                                "price": 3.2
                            }
                        ]
                    },
                    {
                        "key": "spreads",
                        "last_update": "2024-02-23T13:40:35Z",
                        "outcomes": [
                            {
                                "name": "Atlanta Hawks",
                                "price": 1.91,
                                "point": -7.0
                            },
                            {
                                "name": "Toronto Raptors",
                                "price": 1.91,
                                "point": 7.0
                            }
                        ]
                    },
                    {
                        "key": "totals",
                        "last_update": "2024-02-23T13:40:35Z",
                        "outcomes": [
                            {
                                "name": "Over",
                                "price": 1.91,
                                "point": 245.5
                            },
                            {
                                "name": "Under",
                                "price": 1.91,
                                "point": 245.5
                            }
                        ]
                    }
                ]
            },
            {
                "key": "fanduel",
                "title": "FanDuel",
                "last_update": "2024-02-23T13:40:06Z",
                "markets": [
                    {
                        "key": "h2h",
                        "last_update": "2024-02-23T13:40:06Z",
                        "outcomes": [
                            {
                                "name": "Atlanta Hawks",
                                "price": 1.34
                            },
                            {
                                "name": "Toronto Raptors",
                                "price": 3.35
                            }
                        ]
                    },
                    {
                        "key": "spreads",
                        "last_update": "2024-02-23T13:40:06Z",
                        "outcomes": [
                            {
                                "name": "Atlanta Hawks",
                                "price": 1.91,
                                "point": -7.0
                            },
                            {
                                "name": "Toronto Raptors",
                                "price": 1.91,
                                "point": 7.0
                            }
                        ]
                    },
                    {
                        "key": "totals",
                        "last_update": "2024-02-23T13:40:06Z",
                        "outcomes": [
                            {
                                "name": "Over",
                                "price": 1.93,
                                "point": 245.0
                            },
                            {
                                "name": "Under",
                                "price": 1.89,
                                "point": 245.0
                            }
                        ]
                    }
                ]
            },
            {
                "key": "bovada",
                "title": "Bovada",
                "last_update": "2024-02-23T13:41:03Z",
                "markets": [
                    {
                        "key": "h2h",
                        "last_update": "2024-02-23T13:41:03Z",
                        "outcomes": [
                            {
                                "name": "Atlanta Hawks",
                                "price": 1.36
                            },
                            {
                                "name": "Toronto Raptors",
                                "price": 3.3
                            }
                        ]
                    },
                    {
                        "key": "spreads",
                        "last_update": "2024-02-23T13:41:03Z",
                        "outcomes": [
                            {
                                "name": "Atlanta Hawks",
                                "price": 1.91,
                                "point": -7.0
                            },
                            {
                                "name": "Toronto Raptors",
                                "price": 1.91,
                                "point": 7.0
                            }
                        ]
                    },
                    {
                        "key": "totals",
                        "last_update": "2024-02-23T13:41:03Z",
                        "outcomes": [
                            {
                                "name": "Over",
                                "price": 1.91,
                                "point": 245.5
                            },
                            {
                                "name": "Under",
                                "price": 1.91,
                                "point": 245.5
                            }
                        ]
                    }
                ]
            },
            {
                "key": "betmgm",
                "title": "BetMGM",
                "last_update": "2024-02-23T13:38:20Z",
                "markets": [
                    {
                        "key": "h2h",
                        "last_update": "2024-02-23T13:38:20Z",
                        "outcomes": [
                            {
                                "name": "Atlanta Hawks",
                                "price": 1.36
                            },
                            {
                                "name": "Toronto Raptors",
                                "price": 3.2
                            }
                        ]
                    },
                    {
                        "key": "spreads",
                        "last_update": "2024-02-23T13:38:20Z",
                        "outcomes": [
                            {
                                "name": "Atlanta Hawks",
                                "price": 1.87,
                                "point": -6.5
                            },
                            {
                                "name": "Toronto Raptors",
                                "price": 1.95,
                                "point": 6.5
                            }
                        ]
                    },
                    {
                        "key": "totals",
                        "last_update": "2024-02-23T13:38:20Z",
                        "outcomes": [
                            {
                                "name": "Over",
                                "price": 1.91,
                                "point": 245.5
                            },
                            {
                                "name": "Under",
                                "price": 1.91,
                                "point": 245.5
                            }
                        ]
                    }
                ]
            },
            {
                "key": "unibet_us",
                "title": "Unibet",
                "last_update": "2024-02-23T13:40:36Z",
                "markets": [
                    {
                        "key": "h2h",
                        "last_update": "2024-02-23T13:40:36Z",
                        "outcomes": [
                            {
                                "name": "Atlanta Hawks",
                                "price": 1.35
                            },
                            {
                                "name": "Toronto Raptors",
                                "price": 3.35
                            }
                        ]
                    },
                    {
                        "key": "spreads",
                        "last_update": "2024-02-23T13:40:36Z",
                        "outcomes": [
                            {
                                "name": "Atlanta Hawks",
                                "price": 1.89,
                                "point": -7.0
                            },
                            {
                                "name": "Toronto Raptors",
                                "price": 1.92,
                                "point": 7.0
                            }
                        ]
                    },
                    {
                        "key": "totals",
                        "last_update": "2024-02-23T13:40:36Z",
                        "outcomes": [
                            {
                                "name": "Over",
                                "price": 1.89,
                                "point": 245.0
                            },
                            {
                                "name": "Under",
                                "price": 1.92,
                                "point": 245.0
                            }
                        ]
                    }
                ]
            },
            {
                "key": "betrivers",
                "title": "BetRivers",
                "last_update": "2024-02-23T13:40:36Z",
                "markets": [
                    {
                        "key": "h2h",
                        "last_update": "2024-02-23T13:40:36Z",
                        "outcomes": [
                            {
                                "name": "Atlanta Hawks",
                                "price": 1.35
                            },
                            {
                                "name": "Toronto Raptors",
                                "price": 3.35
                            }
                        ]
                    },
                    {
                        "key": "spreads",
                        "last_update": "2024-02-23T13:40:36Z",
                        "outcomes": [
                            {
                                "name": "Atlanta Hawks",
                                "price": 1.89,
                                "point": -7.0
                            },
                            {
                                "name": "Toronto Raptors",
                                "price": 1.92,
                                "point": 7.0
                            }
                        ]
                    },
                    {
                        "key": "totals",
                        "last_update": "2024-02-23T13:40:36Z",
                        "outcomes": [
                            {
                                "name": "Over",
                                "price": 1.89,
                                "point": 245.0
                            },
                            {
                                "name": "Under",
                                "price": 1.92,
                                "point": 245.0
                            }
                        ]
                    }
                ]
            },
            {
                "key": "betus",
                "title": "BetUS",
                "last_update": "2024-02-23T13:40:36Z",
                "markets": [
                    {
                        "key": "h2h",
                        "last_update": "2024-02-23T13:40:36Z",
                        "outcomes": [
                            {
                                "name": "Atlanta Hawks",
                                "price": 1.36
                            },
                            {
                                "name": "Toronto Raptors",
                                "price": 3.25
                            }
                        ]
                    },
                    {
                        "key": "spreads",
                        "last_update": "2024-02-23T13:40:36Z",
                        "outcomes": [
                            {
                                "name": "Atlanta Hawks",
                                "price": 1.91,
                                "point": -7.0
                            },
                            {
                                "name": "Toronto Raptors",
                                "price": 1.91,
                                "point": 7.0
                            }
                        ]
                    },
                    {
                        "key": "totals",
                        "last_update": "2024-02-23T13:40:36Z",
                        "outcomes": [
                            {
                                "name": "Over",
                                "price": 1.91,
                                "point": 245.5
                            },
                            {
                                "name": "Under",
                                "price": 1.91,
                                "point": 245.5
                            }
                        ]
                    }
                ]
            }
        ]
    },
    {
        "id": "f695fc5d725bc275343391fb87ed861e",
        "sport_key": "basketball_nba",
        "sport_title": "NBA",
        "commence_time": "2024-02-24T00:40:00Z",
        "home_team": "Philadelphia 76ers",
        "away_team": "Cleveland Cavaliers",
        "bookmakers": [
            {
                "key": "draftkings",
                "title": "DraftKings",
                "last_update": "2024-02-23T13:40:35Z",
                "markets": [
                    {
                        "key": "h2h",
                        "last_update": "2024-02-23T13:40:35Z",
                        "outcomes": [
                            {
                                "name": "Cleveland Cavaliers",
                                "price": 1.6
                            },
                            {
                                "name": "Philadelphia 76ers",
                                "price": 2.4
                            }
                        ]
                    },
                    {
                        "key": "spreads",
                        "last_update": "2024-02-23T13:40:35Z",
                        "outcomes": [
                            {
                                "name": "Cleveland Cavaliers",
                                "price": 1.91,
                                "point": -3.5
                            },
                            {
                                "name": "Philadelphia 76ers",
                                "price": 1.91,
                                "point": 3.5
                            }
                        ]
                    },
                    {
                        "key": "totals",
                        "last_update": "2024-02-23T13:40:35Z",
                        "outcomes": [
                            {
                                "name": "Over",
                                "price": 1.89,
                                "point": 228.0
                            },
                            {
                                "name": "Under",
                                "price": 1.93,
                                "point": 228.0
                            }
                        ]
                    }
                ]
            },
            {
                "key": "pointsbetus",
                "title": "PointsBet (US)",
                "last_update": "2024-02-23T13:40:35Z",
                "markets": [
                    {
                        "key": "h2h",
                        "last_update": "2024-02-23T13:40:35Z",
                        "outcomes": [
                            {
                                "name": "Cleveland Cavaliers",
                                "price": 1.59
                            },
                            {
                                "name": "Philadelphia 76ers",
                                "price": 2.4
                            }
                        ]
                    },
                    {
                        "key": "spreads",
                        "last_update": "2024-02-23T13:40:35Z",
                        "outcomes": [
                            {
                                "name": "Cleveland Cavaliers",
                                "price": 1.91,
                                "point": -4.0
                            },
                            {
                                "name": "Philadelphia 76ers",
                                "price": 1.91,
                                "point": 4.0
                            }
                        ]
                    },
                    {
                        "key": "totals",
                        "last_update": "2024-02-23T13:40:35Z",
                        "outcomes": [
                            {
                                "name": "Over",
                                "price": 1.91,
                                "point": 228.0
                            },
                            {
                                "name": "Under",
                                "price": 1.91,
                                "point": 228.0
                            }
                        ]
                    }
                ]
            },
            {
                "key": "wynnbet",
                "title": "WynnBET",
                "last_update": "2024-02-23T13:41:03Z",
                "markets": [
                    {
                        "key": "h2h",
                        "last_update": "2024-02-23T13:41:03Z",
                        "outcomes": [
                            {
                                "name": "Cleveland Cavaliers",
                                "price": 1.59
                            },
                            {
                                "name": "Philadelphia 76ers",
                                "price": 2.45
                            }
                        ]
                    },
                    {
                        "key": "spreads",
                        "last_update": "2024-02-23T13:41:03Z",
                        "outcomes": [
                            {
                                "name": "Cleveland Cavaliers",
                                "price": 1.91,
                                "point": -3.5
                            },
                            {
                                "name": "Philadelphia 76ers",
                                "price": 1.91,
                                "point": 3.5
                            }
                        ]
                    },
                    {
                        "key": "totals",
                        "last_update": "2024-02-23T13:41:03Z",
                        "outcomes": [
                            {
                                "name": "Over",
                                "price": 1.91,
                                "point": 228.0
                            },
                            {
                                "name": "Under",
                                "price": 1.91,
                                "point": 228.0
                            }
                        ]
                    }
                ]
            },
            {
                "key": "fanduel",
                "title": "FanDuel",
                "last_update": "2024-02-23T13:40:06Z",
                "markets": [
                    {
                        "key": "h2h",
                        "last_update": "2024-02-23T13:40:06Z",
                        "outcomes": [
                            {
                                "name": "Cleveland Cavaliers",
                                "price": 1.66
                            },
                            {
                                "name": "Philadelphia 76ers",
                                "price": 2.28
                            }
                        ]
                    },
                    {
                        "key": "spreads",
                        "last_update": "2024-02-23T13:40:06Z",
                        "outcomes": [
                            {
                                "name": "Cleveland Cavaliers",
                                "price": 1.91,
                                "point": -3.5
                            },
                            {
                                "name": "Philadelphia 76ers",
                                "price": 1.91,
                                "point": 3.5
                            }
                        ]
                    },
                    {
                        "key": "totals",
                        "last_update": "2024-02-23T13:40:06Z",
                        "outcomes": [
                            {
                                "name": "Over",
                                "price": 1.91,
                                "point": 228.0
                            },
                            {
                                "name": "Under",
                                "price": 1.91,
                                "point": 228.0
                            }
                        ]
                    }
                ]
            },
            {
                "key": "mybookieag",
                "title": "MyBookie.ag",
                "last_update": "2024-02-23T13:40:35Z",
                "markets": [
                    {
                        "key": "h2h",
                        "last_update": "2024-02-23T13:40:35Z",
                        "outcomes": [
                            {
                                "name": "Cleveland Cavaliers",
                                "price": 1.59
                            },
                            {
                                "name": "Philadelphia 76ers",
                                "price": 2.45
                            }
                        ]
                    },
                    {
                        "key": "spreads",
                        "last_update": "2024-02-23T13:40:35Z",
                        "outcomes": [
                            {
                                "name": "Cleveland Cavaliers",
                                "price": 1.91,
                                "point": -4.0
                            },
                            {
                                "name": "Philadelphia 76ers",
                                "price": 1.91,
                                "point": 4.0
                            }
                        ]
                    },
                    {
                        "key": "totals",
                        "last_update": "2024-02-23T13:40:35Z",
                        "outcomes": [
                            {
                                "name": "Over",
                                "price": 1.91,
                                "point": 228.0
                            },
                            {
                                "name": "Under",
                                "price": 1.91,
                                "point": 228.0
                            }
                        ]
                    }
                ]
            },
            {
                "key": "betmgm",
                "title": "BetMGM",
                "last_update": "2024-02-23T13:38:20Z",
                "markets": [
                    {
                        "key": "h2h",
                        "last_update": "2024-02-23T13:38:20Z",
                        "outcomes": [
                            {
                                "name": "Cleveland Cavaliers",
                                "price": 1.61
                            },
                            {
                                "name": "Philadelphia 76ers",
                                "price": 2.4
                            }
                        ]
                    },
                    {
                        "key": "spreads",
                        "last_update": "2024-02-23T13:38:20Z",
                        "outcomes": [
                            {
                                "name": "Cleveland Cavaliers",
                                "price": 1.91,
                                "point": -3.5
                            },
                            {
                                "name": "Philadelphia 76ers",
                                "price": 1.91,
                                "point": 3.5
                            }
                        ]
                    },
                    {
                        "key": "totals",
                        "last_update": "2024-02-23T13:38:20Z",
                        "outcomes": [
                            {
                                "name": "Over",
                                "price": 1.87,
                                "point": 227.5
                            },
                            {
                                "name": "Under",
                                "price": 1.95,
                                "point": 227.5
                            }
                        ]
                    }
                ]
            },
            {
                "key": "unibet_us",
                "title": "Unibet",
                "last_update": "2024-02-23T13:40:36Z",
                "markets": [
                    {
                        "key": "h2h",
                        "last_update": "2024-02-23T13:40:36Z",
                        "outcomes": [
                            {
                                "name": "Cleveland Cavaliers",
                                "price": 1.57
                            },
                            {
                                "name": "Philadelphia 76ers",
                                "price": 2.45
                            }
                        ]
                    },
                    {
                        "key": "spreads",
                        "last_update": "2024-02-23T13:40:36Z",
                        "outcomes": [
                            {
                                "name": "Cleveland Cavaliers",
                                "price": 1.92,
                                "point": -4.0
                            },
                            {
                                "name": "Philadelphia 76ers",
                                "price": 1.89,
                                "point": 4.0
                            }
                        ]
                    },
                    {
                        "key": "totals",
                        "last_update": "2024-02-23T13:40:36Z",
                        "outcomes": [
                            {
                                "name": "Over",
                                "price": 1.91,
                                "point": 228.0
                            },
                            {
                                "name": "Under",
                                "price": 1.91,
                                "point": 228.0
                            }
                        ]
                    }
                ]
            },
            {
                "key": "betrivers",
                "title": "BetRivers",
                "last_update": "2024-02-23T13:40:36Z",
                "markets": [
                    {
                        "key": "h2h",
                        "last_update": "2024-02-23T13:40:36Z",
                        "outcomes": [
                            {
                                "name": "Cleveland Cavaliers",
                                "price": 1.57
                            },
                            {
                                "name": "Philadelphia 76ers",
                                "price": 2.45
                            }
                        ]
                    },
                    {
                        "key": "spreads",
                        "last_update": "2024-02-23T13:40:36Z",
                        "outcomes": [
                            {
                                "name": "Cleveland Cavaliers",
                                "price": 1.92,
                                "point": -4.0
                            },
                            {
                                "name": "Philadelphia 76ers",
                                "price": 1.89,
                                "point": 4.0
                            }
                        ]
                    },
                    {
                        "key": "totals",
                        "last_update": "2024-02-23T13:40:36Z",
                        "outcomes": [
                            {
                                "name": "Over",
                                "price": 1.91,
                                "point": 228.0
                            },
                            {
                                "name": "Under",
                                "price": 1.91,
                                "point": 228.0
                            }
                        ]
                    }
                ]
            },
            {
                "key": "williamhill_us",
                "title": "Caesars",
                "last_update": "2024-02-23T13:38:20Z",
                "markets": [
                    {
                        "key": "h2h",
                        "last_update": "2024-02-23T13:38:20Z",
                        "outcomes": [
                            {
                                "name": "Cleveland Cavaliers",
                                "price": 1.61
                            },
                            {
                                "name": "Philadelphia 76ers",
                                "price": 2.4
                            }
                        ]
                    },
                    {
                        "key": "spreads",
                        "last_update": "2024-02-23T13:38:20Z",
                        "outcomes": [
                            {
                                "name": "Cleveland Cavaliers",
                                "price": 1.91,
                                "point": -3.5
                            },
                            {
                                "name": "Philadelphia 76ers",
                                "price": 1.91,
                                "point": 3.5
                            }
                        ]
                    },
                    {
                        "key": "totals",
                        "last_update": "2024-02-23T13:38:20Z",
                        "outcomes": [
                            {
                                "name": "Over",
                                "price": 1.91,
                                "point": 228.0
                            },
                            {
                                "name": "Under",
                                "price": 1.91,
                                "point": 228.0
                            }
                        ]
                    }
                ]
            },
            {
                "key": "bovada",
                "title": "Bovada",
                "last_update": "2024-02-23T13:41:03Z",
                "markets": [
                    {
                        "key": "h2h",
                        "last_update": "2024-02-23T13:41:03Z",
                        "outcomes": [
                            {
                                "name": "Cleveland Cavaliers",
                                "price": 1.62
                            },
                            {
                                "name": "Philadelphia 76ers",
                                "price": 2.35
                            }
                        ]
                    },
                    {
                        "key": "spreads",
                        "last_update": "2024-02-23T13:41:03Z",
                        "outcomes": [
                            {
                                "name": "Cleveland Cavaliers",
                                "price": 1.91,
                                "point": -3.5
                            },
                            {
                                "name": "Philadelphia 76ers",
                                "price": 1.91,
                                "point": 3.5
                            }
                        ]
                    },
                    {
                        "key": "totals",
                        "last_update": "2024-02-23T13:41:03Z",
                        "outcomes": [
                            {
                                "name": "Over",
                                "price": 1.87,
                                "point": 228.0
                            },
                            {
                                "name": "Under",
                                "price": 1.95,
                                "point": 228.0
                            }
                        ]
                    }
                ]
            },
            {
                "key": "betonlineag",
                "title": "BetOnline.ag",
                "last_update": "2024-02-23T13:40:35Z",
                "markets": [
                    {
                        "key": "h2h",
                        "last_update": "2024-02-23T13:40:35Z",
                        "outcomes": [
                            {
                                "name": "Cleveland Cavaliers",
                                "price": 1.62
                            },
                            {
                                "name": "Philadelphia 76ers",
                                "price": 2.4
                            }
                        ]
                    },
                    {
                        "key": "spreads",
                        "last_update": "2024-02-23T13:40:35Z",
                        "outcomes": [
                            {
                                "name": "Cleveland Cavaliers",
                                "price": 1.91,
                                "point": -3.5
                            },
                            {
                                "name": "Philadelphia 76ers",
                                "price": 1.91,
                                "point": 3.5
                            }
                        ]
                    },
                    {
                        "key": "totals",
                        "last_update": "2024-02-23T13:40:35Z",
                        "outcomes": [
                            {
                                "name": "Over",
                                "price": 1.91,
                                "point": 228.0
                            },
                            {
                                "name": "Under",
                                "price": 1.91,
                                "point": 228.0
                            }
                        ]
                    }
                ]
            },
            {
                "key": "lowvig",
                "title": "LowVig.ag",
                "last_update": "2024-02-23T13:41:04Z",
                "markets": [
                    {
                        "key": "h2h",
                        "last_update": "2024-02-23T13:41:04Z",
                        "outcomes": [
                            {
                                "name": "Cleveland Cavaliers",
                                "price": 1.62
                            },
                            {
                                "name": "Philadelphia 76ers",
                                "price": 2.4
                            }
                        ]
                    },
                    {
                        "key": "spreads",
                        "last_update": "2024-02-23T13:41:04Z",
                        "outcomes": [
                            {
                                "name": "Cleveland Cavaliers",
                                "price": 1.94,
                                "point": -3.5
                            },
                            {
                                "name": "Philadelphia 76ers",
                                "price": 1.94,
                                "point": 3.5
                            }
                        ]
                    },
                    {
                        "key": "totals",
                        "last_update": "2024-02-23T13:41:04Z",
                        "outcomes": [
                            {
                                "name": "Over",
                                "price": 1.94,
                                "point": 228.0
                            },
                            {
                                "name": "Under",
                                "price": 1.94,
                                "point": 228.0
                            }
                        ]
                    }
                ]
            },
            {
                "key": "betus",
                "title": "BetUS",
                "last_update": "2024-02-23T13:40:36Z",
                "markets": [
                    {
                        "key": "h2h",
                        "last_update": "2024-02-23T13:40:36Z",
                        "outcomes": [
                            {
                                "name": "Cleveland Cavaliers",
                                "price": 1.61
                            },
                            {
                                "name": "Philadelphia 76ers",
                                "price": 2.45
                            }
                        ]
                    },
                    {
                        "key": "spreads",
                        "last_update": "2024-02-23T13:40:36Z",
                        "outcomes": [
                            {
                                "name": "Cleveland Cavaliers",
                                "price": 1.91,
                                "point": -3.5
                            },
                            {
                                "name": "Philadelphia 76ers",
                                "price": 1.91,
                                "point": 3.5
                            }
                        ]
                    },
                    {
                        "key": "totals",
                        "last_update": "2024-02-23T13:40:36Z",
                        "outcomes": [
                            {
                                "name": "Over",
                                "price": 1.91,
                                "point": 228.0
                            },
                            {
                                "name": "Under",
                                "price": 1.91,
                                "point": 228.0
                            }
                        ]
                    }
                ]
            }
        ]
    },
    {
        "id": "59df473d0ef251265245d62b7adeb30e",
        "sport_key": "basketball_nba",
        "sport_title": "NBA",
        "commence_time": "2024-02-24T01:10:00Z",
        "home_team": "Houston Rockets",
        "away_team": "Phoenix Suns",
        "bookmakers": [
            {
                "key": "draftkings",
                "title": "DraftKings",
                "last_update": "2024-02-23T13:40:35Z",
                "markets": [
                    {
                        "key": "h2h",
                        "last_update": "2024-02-23T13:40:35Z",
                        "outcomes": [
                            {
                                "name": "Houston Rockets",
                                "price": 2.36
                            },
                            {
                                "name": "Phoenix Suns",
                                "price": 1.62
                            }
                        ]
                    },
                    {
                        "key": "spreads",
                        "last_update": "2024-02-23T13:40:35Z",
                        "outcomes": [
                            {
                                "name": "Houston Rockets",
                                "price": 1.93,
                                "point": 3.5
                            },
                            {
                                "name": "Phoenix Suns",
                                "price": 1.89,
                                "point": -3.5
                            }
                        ]
                    },
                    {
                        "key": "totals",
                        "last_update": "2024-02-23T13:40:35Z",
                        "outcomes": [
                            {
                                "name": "Over",
                                "price": 1.93,
                                "point": 233.5
                            },
                            {
                                "name": "Under",
                                "price": 1.89,
                                "point": 233.5
                            }
                        ]
                    }
                ]
            },
            {
                "key": "fanduel",
                "title": "FanDuel",
                "last_update": "2024-02-23T13:40:06Z",
                "markets": [
                    {
                        "key": "h2h",
                        "last_update": "2024-02-23T13:40:06Z",
                        "outcomes": [
                            {
                                "name": "Houston Rockets",
                                "price": 2.46
                            },
                            {
                                "name": "Phoenix Suns",
                                "price": 1.57
                            }
                        ]
                    },
                    {
                        "key": "spreads",
                        "last_update": "2024-02-23T13:40:06Z",
                        "outcomes": [
                            {
                                "name": "Houston Rockets",
                                "price": 1.91,
                                "point": 4.0
                            },
                            {
                                "name": "Phoenix Suns",
                                "price": 1.91,
                                "point": -4.0
                            }
                        ]
                    },
                    {
                        "key": "totals",
                        "last_update": "2024-02-23T13:40:06Z",
                        "outcomes": [
                            {
                                "name": "Over",
                                "price": 1.91,
                                "point": 233.5
                            },
                            {
                                "name": "Under",
                                "price": 1.91,
                                "point": 233.5
                            }
                        ]
                    }
                ]
            },
            {
                "key": "pointsbetus",
                "title": "PointsBet (US)",
                "last_update": "2024-02-23T13:40:35Z",
                "markets": [
                    {
                        "key": "h2h",
                        "last_update": "2024-02-23T13:40:35Z",
                        "outcomes": [
                            {
                                "name": "Houston Rockets",
                                "price": 2.3
                            },
                            {
                                "name": "Phoenix Suns",
                                "price": 1.62
                            }
                        ]
                    },
                    {
                        "key": "spreads",
                        "last_update": "2024-02-23T13:40:35Z",
                        "outcomes": [
                            {
                                "name": "Houston Rockets",
                                "price": 1.91,
                                "point": 4.0
                            },
                            {
                                "name": "Phoenix Suns",
                                "price": 1.91,
                                "point": -4.0
                            }
                        ]
                    },
                    {
                        "key": "totals",
                        "last_update": "2024-02-23T13:40:35Z",
                        "outcomes": [
                            {
                                "name": "Over",
                                "price": 1.91,
                                "point": 233.5
                            },
                            {
                                "name": "Under",
                                "price": 1.91,
                                "point": 233.5
                            }
                        ]
                    }
                ]
            },
            {
                "key": "wynnbet",
                "title": "WynnBET",
                "last_update": "2024-02-23T13:41:03Z",
                "markets": [
                    {
                        "key": "h2h",
                        "last_update": "2024-02-23T13:41:03Z",
                        "outcomes": [
                            {
                                "name": "Houston Rockets",
                                "price": 2.4
                            },
                            {
                                "name": "Phoenix Suns",
                                "price": 1.62
                            }
                        ]
                    },
                    {
                        "key": "spreads",
                        "last_update": "2024-02-23T13:41:03Z",
                        "outcomes": [
                            {
                                "name": "Houston Rockets",
                                "price": 1.91,
                                "point": 3.5
                            },
                            {
                                "name": "Phoenix Suns",
                                "price": 1.91,
                                "point": -3.5
                            }
                        ]
                    },
                    {
                        "key": "totals",
                        "last_update": "2024-02-23T13:41:03Z",
                        "outcomes": [
                            {
                                "name": "Over",
                                "price": 1.91,
                                "point": 233.5
                            },
                            {
                                "name": "Under",
                                "price": 1.91,
                                "point": 233.5
                            }
                        ]
                    }
                ]
            },
            {
                "key": "mybookieag",
                "title": "MyBookie.ag",
                "last_update": "2024-02-23T13:40:35Z",
                "markets": [
                    {
                        "key": "h2h",
                        "last_update": "2024-02-23T13:40:35Z",
                        "outcomes": [
                            {
                                "name": "Houston Rockets",
                                "price": 2.4
                            },
                            {
                                "name": "Phoenix Suns",
                                "price": 1.62
                            }
                        ]
                    },
                    {
                        "key": "spreads",
                        "last_update": "2024-02-23T13:40:35Z",
                        "outcomes": [
                            {
                                "name": "Houston Rockets",
                                "price": 1.91,
                                "point": 3.5
                            },
                            {
                                "name": "Phoenix Suns",
                                "price": 1.91,
                                "point": -3.5
                            }
                        ]
                    },
                    {
                        "key": "totals",
                        "last_update": "2024-02-23T13:40:35Z",
                        "outcomes": [
                            {
                                "name": "Over",
                                "price": 1.91,
                                "point": 233.5
                            },
                            {
                                "name": "Under",
                                "price": 1.91,
                                "point": 233.5
                            }
                        ]
                    }
                ]
            },
            {
                "key": "betmgm",
                "title": "BetMGM",
                "last_update": "2024-02-23T13:38:20Z",
                "markets": [
                    {
                        "key": "h2h",
                        "last_update": "2024-02-23T13:38:20Z",
                        "outcomes": [
                            {
                                "name": "Houston Rockets",
                                "price": 2.35
                            },
                            {
                                "name": "Phoenix Suns",
                                "price": 1.61
                            }
                        ]
                    },
                    {
                        "key": "spreads",
                        "last_update": "2024-02-23T13:38:20Z",
                        "outcomes": [
                            {
                                "name": "Houston Rockets",
                                "price": 1.91,
                                "point": 3.5
                            },
                            {
                                "name": "Phoenix Suns",
                                "price": 1.91,
                                "point": -3.5
                            }
                        ]
                    },
                    {
                        "key": "totals",
                        "last_update": "2024-02-23T13:38:20Z",
                        "outcomes": [
                            {
                                "name": "Over",
                                "price": 1.91,
                                "point": 233.5
                            },
                            {
                                "name": "Under",
                                "price": 1.91,
                                "point": 233.5
                            }
                        ]
                    }
                ]
            },
            {
                "key": "betrivers",
                "title": "BetRivers",
                "last_update": "2024-02-23T13:40:36Z",
                "markets": [
                    {
                        "key": "h2h",
                        "last_update": "2024-02-23T13:40:36Z",
                        "outcomes": [
                            {
                                "name": "Houston Rockets",
                                "price": 2.4
                            },
                            {
                                "name": "Phoenix Suns",
                                "price": 1.6
                            }
                        ]
                    },
                    {
                        "key": "spreads",
                        "last_update": "2024-02-23T13:40:36Z",
                        "outcomes": [
                            {
                                "name": "Houston Rockets",
                                "price": 1.88,
                                "point": 4.0
                            },
                            {
                                "name": "Phoenix Suns",
                                "price": 1.93,
                                "point": -4.0
                            }
                        ]
                    },
                    {
                        "key": "totals",
                        "last_update": "2024-02-23T13:40:36Z",
                        "outcomes": [
                            {
                                "name": "Over",
                                "price": 1.88,
                                "point": 233.0
                            },
                            {
                                "name": "Under",
                                "price": 1.93,
                                "point": 233.0
                            }
                        ]
                    }
                ]
            },
            {
                "key": "unibet_us",
                "title": "Unibet",
                "last_update": "2024-02-23T13:40:36Z",
                "markets": [
                    {
                        "key": "h2h",
                        "last_update": "2024-02-23T13:40:36Z",
                        "outcomes": [
                            {
                                "name": "Houston Rockets",
                                "price": 2.4
                            },
                            {
                                "name": "Phoenix Suns",
                                "price": 1.6
                            }
                        ]
                    },
                    {
                        "key": "spreads",
                        "last_update": "2024-02-23T13:40:36Z",
                        "outcomes": [
                            {
                                "name": "Houston Rockets",
                                "price": 1.88,
                                "point": 4.0
                            },
                            {
                                "name": "Phoenix Suns",
                                "price": 1.93,
                                "point": -4.0
                            }
                        ]
                    },
                    {
                        "key": "totals",
                        "last_update": "2024-02-23T13:40:36Z",
                        "outcomes": [
                            {
                                "name": "Over",
                                "price": 1.88,
                                "point": 233.0
                            },
                            {
                                "name": "Under",
                                "price": 1.93,
                                "point": 233.0
                            }
                        ]
                    }
                ]
            },
            {
                "key": "williamhill_us",
                "title": "Caesars",
                "last_update": "2024-02-23T13:38:20Z",
                "markets": [
                    {
                        "key": "h2h",
                        "last_update": "2024-02-23T13:38:20Z",
                        "outcomes": [
                            {
                                "name": "Houston Rockets",
                                "price": 2.4
                            },
                            {
                                "name": "Phoenix Suns",
                                "price": 1.61
                            }
                        ]
                    },
                    {
                        "key": "spreads",
                        "last_update": "2024-02-23T13:38:20Z",
                        "outcomes": [
                            {
                                "name": "Houston Rockets",
                                "price": 1.91,
                                "point": 3.5
                            },
                            {
                                "name": "Phoenix Suns",
                                "price": 1.91,
                                "point": -3.5
                            }
                        ]
                    },
                    {
                        "key": "totals",
                        "last_update": "2024-02-23T13:38:20Z",
                        "outcomes": [
                            {
                                "name": "Over",
                                "price": 1.91,
                                "point": 233.5
                            },
                            {
                                "name": "Under",
                                "price": 1.91,
                                "point": 233.5
                            }
                        ]
                    }
                ]
            },
            {
                "key": "bovada",
                "title": "Bovada",
                "last_update": "2024-02-23T13:41:03Z",
                "markets": [
                    {
                        "key": "h2h",
                        "last_update": "2024-02-23T13:41:03Z",
                        "outcomes": [
                            {
                                "name": "Houston Rockets",
                                "price": 2.45
                            },
                            {
                                "name": "Phoenix Suns",
                                "price": 1.59
                            }
                        ]
                    },
                    {
                        "key": "spreads",
                        "last_update": "2024-02-23T13:41:03Z",
                        "outcomes": [
                            {
                                "name": "Houston Rockets",
                                "price": 1.91,
                                "point": 4.0
                            },
                            {
                                "name": "Phoenix Suns",
                                "price": 1.91,
                                "point": -4.0
                            }
                        ]
                    },
                    {
                        "key": "totals",
                        "last_update": "2024-02-23T13:41:03Z",
                        "outcomes": [
                            {
                                "name": "Over",
                                "price": 1.87,
                                "point": 232.5
                            },
                            {
                                "name": "Under",
                                "price": 1.95,
                                "point": 232.5
                            }
                        ]
                    }
                ]
            },
            {
                "key": "betus",
                "title": "BetUS",
                "last_update": "2024-02-23T13:40:36Z",
                "markets": [
                    {
                        "key": "h2h",
                        "last_update": "2024-02-23T13:40:36Z",
                        "outcomes": [
                            {
                                "name": "Houston Rockets",
                                "price": 2.45
                            },
                            {
                                "name": "Phoenix Suns",
                                "price": 1.61
                            }
                        ]
                    },
                    {
                        "key": "spreads",
                        "last_update": "2024-02-23T13:40:36Z",
                        "outcomes": [
                            {
                                "name": "Houston Rockets",
                                "price": 1.91,
                                "point": 3.5
                            },
                            {
                                "name": "Phoenix Suns",
                                "price": 1.91,
                                "point": -3.5
                            }
                        ]
                    },
                    {
                        "key": "totals",
                        "last_update": "2024-02-23T13:40:36Z",
                        "outcomes": [
                            {
                                "name": "Over",
                                "price": 1.91,
                                "point": 233.5
                            },
                            {
                                "name": "Under",
                                "price": 1.91,
                                "point": 233.5
                            }
                        ]
                    }
                ]
            },
            {
                "key": "betonlineag",
                "title": "BetOnline.ag",
                "last_update": "2024-02-23T13:40:35Z",
                "markets": [
                    {
                        "key": "h2h",
                        "last_update": "2024-02-23T13:40:35Z",
                        "outcomes": [
                            {
                                "name": "Houston Rockets",
                                "price": 2.45
                            },
                            {
                                "name": "Phoenix Suns",
                                "price": 1.61
                            }
                        ]
                    },
                    {
                        "key": "spreads",
                        "last_update": "2024-02-23T13:40:35Z",
                        "outcomes": [
                            {
                                "name": "Houston Rockets",
                                "price": 1.93,
                                "point": 3.5
                            },
                            {
                                "name": "Phoenix Suns",
                                "price": 1.89,
                                "point": -3.5
                            }
                        ]
                    },
                    {
                        "key": "totals",
                        "last_update": "2024-02-23T13:40:35Z",
                        "outcomes": [
                            {
                                "name": "Over",
                                "price": 1.91,
                                "point": 233.5
                            },
                            {
                                "name": "Under",
                                "price": 1.91,
                                "point": 233.5
                            }
                        ]
                    }
                ]
            },
            {
                "key": "lowvig",
                "title": "LowVig.ag",
                "last_update": "2024-02-23T13:41:04Z",
                "markets": [
                    {
                        "key": "h2h",
                        "last_update": "2024-02-23T13:41:04Z",
                        "outcomes": [
                            {
                                "name": "Houston Rockets",
                                "price": 2.45
                            },
                            {
                                "name": "Phoenix Suns",
                                "price": 1.61
                            }
                        ]
                    },
                    {
                        "key": "spreads",
                        "last_update": "2024-02-23T13:41:04Z",
                        "outcomes": [
                            {
                                "name": "Houston Rockets",
                                "price": 1.96,
                                "point": 3.5
                            },
                            {
                                "name": "Phoenix Suns",
                                "price": 1.93,
                                "point": -3.5
                            }
                        ]
                    },
                    {
                        "key": "totals",
                        "last_update": "2024-02-23T13:41:04Z",
                        "outcomes": [
                            {
                                "name": "Over",
                                "price": 1.94,
                                "point": 233.5
                            },
                            {
                                "name": "Under",
                                "price": 1.94,
                                "point": 233.5
                            }
                        ]
                    }
                ]
            }
        ]
    },
    {
        "id": "2ead771e75ea1ded364c0e9e42ab1404",
        "sport_key": "basketball_nba",
        "sport_title": "NBA",
        "commence_time": "2024-02-24T01:10:00Z",
        "home_team": "Memphis Grizzlies",
        "away_team": "Los Angeles Clippers",
        "bookmakers": [
            {
                "key": "draftkings",
                "title": "DraftKings",
                "last_update": "2024-02-23T13:40:35Z",
                "markets": [
                    {
                        "key": "h2h",
                        "last_update": "2024-02-23T13:40:35Z",
                        "outcomes": [
                            {
                                "name": "Los Angeles Clippers",
                                "price": 1.24
                            },
                            {
                                "name": "Memphis Grizzlies",
                                "price": 4.3
                            }
                        ]
                    },
                    {
                        "key": "spreads",
                        "last_update": "2024-02-23T13:40:35Z",
                        "outcomes": [
                            {
                                "name": "Los Angeles Clippers",
                                "price": 1.89,
                                "point": -9.0
                            },
                            {
                                "name": "Memphis Grizzlies",
                                "price": 1.93,
                                "point": 9.0
                            }
                        ]
                    },
                    {
                        "key": "totals",
                        "last_update": "2024-02-23T13:40:35Z",
                        "outcomes": [
                            {
                                "name": "Over",
                                "price": 1.93,
                                "point": 222.5
                            },
                            {
                                "name": "Under",
                                "price": 1.89,
                                "point": 222.5
                            }
                        ]
                    }
                ]
            },
            {
                "key": "wynnbet",
                "title": "WynnBET",
                "last_update": "2024-02-23T13:41:03Z",
                "markets": [
                    {
                        "key": "h2h",
                        "last_update": "2024-02-23T13:41:03Z",
                        "outcomes": [
                            {
                                "name": "Los Angeles Clippers",
                                "price": 1.25
                            },
                            {
                                "name": "Memphis Grizzlies",
                                "price": 4.2
                            }
                        ]
                    },
                    {
                        "key": "spreads",
                        "last_update": "2024-02-23T13:41:03Z",
                        "outcomes": [
                            {
                                "name": "Los Angeles Clippers",
                                "price": 1.91,
                                "point": -9.0
                            },
                            {
                                "name": "Memphis Grizzlies",
                                "price": 1.91,
                                "point": 9.0
                            }
                        ]
                    },
                    {
                        "key": "totals",
                        "last_update": "2024-02-23T13:41:03Z",
                        "outcomes": [
                            {
                                "name": "Over",
                                "price": 1.91,
                                "point": 222.5
                            },
                            {
                                "name": "Under",
                                "price": 1.91,
                                "point": 222.5
                            }
                        ]
                    }
                ]
            },
            {
                "key": "mybookieag",
                "title": "MyBookie.ag",
                "last_update": "2024-02-23T13:40:35Z",
                "markets": [
                    {
                        "key": "h2h",
                        "last_update": "2024-02-23T13:40:35Z",
                        "outcomes": [
                            {
                                "name": "Los Angeles Clippers",
                                "price": 1.24
                            },
                            {
                                "name": "Memphis Grizzlies",
                                "price": 4.15
                            }
                        ]
                    },
                    {
                        "key": "spreads",
                        "last_update": "2024-02-23T13:40:35Z",
                        "outcomes": [
                            {
                                "name": "Los Angeles Clippers",
                                "price": 1.91,
                                "point": -9.5
                            },
                            {
                                "name": "Memphis Grizzlies",
                                "price": 1.91,
                                "point": 9.5
                            }
                        ]
                    },
                    {
                        "key": "totals",
                        "last_update": "2024-02-23T13:40:35Z",
                        "outcomes": [
                            {
                                "name": "Over",
                                "price": 1.91,
                                "point": 222.5
                            },
                            {
                                "name": "Under",
                                "price": 1.91,
                                "point": 222.5
                            }
                        ]
                    }
                ]
            },
            {
                "key": "fanduel",
                "title": "FanDuel",
                "last_update": "2024-02-23T13:40:06Z",
                "markets": [
                    {
                        "key": "h2h",
                        "last_update": "2024-02-23T13:40:06Z",
                        "outcomes": [
                            {
                                "name": "Los Angeles Clippers",
                                "price": 1.24
                            },
                            {
                                "name": "Memphis Grizzlies",
                                "price": 4.3
                            }
                        ]
                    },
                    {
                        "key": "spreads",
                        "last_update": "2024-02-23T13:40:06Z",
                        "outcomes": [
                            {
                                "name": "Los Angeles Clippers",
                                "price": 1.93,
                                "point": -9.5
                            },
                            {
                                "name": "Memphis Grizzlies",
                                "price": 1.89,
                                "point": 9.5
                            }
                        ]
                    },
                    {
                        "key": "totals",
                        "last_update": "2024-02-23T13:40:06Z",
                        "outcomes": [
                            {
                                "name": "Over",
                                "price": 1.91,
                                "point": 222.5
                            },
                            {
                                "name": "Under",
                                "price": 1.91,
                                "point": 222.5
                            }
                        ]
                    }
                ]
            },
            {
                "key": "pointsbetus",
                "title": "PointsBet (US)",
                "last_update": "2024-02-23T13:40:35Z",
                "markets": [
                    {
                        "key": "h2h",
                        "last_update": "2024-02-23T13:40:35Z",
                        "outcomes": [
                            {
                                "name": "Los Angeles Clippers",
                                "price": 1.24
                            },
                            {
                                "name": "Memphis Grizzlies",
                                "price": 4.3
                            }
                        ]
                    },
                    {
                        "key": "spreads",
                        "last_update": "2024-02-23T13:40:35Z",
                        "outcomes": [
                            {
                                "name": "Los Angeles Clippers",
                                "price": 1.91,
                                "point": -9.0
                            },
                            {
                                "name": "Memphis Grizzlies",
                                "price": 1.91,
                                "point": 9.0
                            }
                        ]
                    },
                    {
                        "key": "totals",
                        "last_update": "2024-02-23T13:40:35Z",
                        "outcomes": [
                            {
                                "name": "Over",
                                "price": 1.91,
                                "point": 222.5
                            },
                            {
                                "name": "Under",
                                "price": 1.91,
                                "point": 222.5
                            }
                        ]
                    }
                ]
            },
            {
                "key": "betmgm",
                "title": "BetMGM",
                "last_update": "2024-02-23T13:38:20Z",
                "markets": [
                    {
                        "key": "h2h",
                        "last_update": "2024-02-23T13:38:20Z",
                        "outcomes": [
                            {
                                "name": "Los Angeles Clippers",
                                "price": 1.25
                            },
                            {
                                "name": "Memphis Grizzlies",
                                "price": 4.1
                            }
                        ]
                    },
                    {
                        "key": "spreads",
                        "last_update": "2024-02-23T13:38:20Z",
                        "outcomes": [
                            {
                                "name": "Los Angeles Clippers",
                                "price": 1.95,
                                "point": -9.5
                            },
                            {
                                "name": "Memphis Grizzlies",
                                "price": 1.87,
                                "point": 9.5
                            }
                        ]
                    },
                    {
                        "key": "totals",
                        "last_update": "2024-02-23T13:38:20Z",
                        "outcomes": [
                            {
                                "name": "Over",
                                "price": 1.91,
                                "point": 222.5
                            },
                            {
                                "name": "Under",
                                "price": 1.91,
                                "point": 222.5
                            }
                        ]
                    }
                ]
            },
            {
                "key": "betrivers",
                "title": "BetRivers",
                "last_update": "2024-02-23T13:40:36Z",
                "markets": [
                    {
                        "key": "h2h",
                        "last_update": "2024-02-23T13:40:36Z",
                        "outcomes": [
                            {
                                "name": "Los Angeles Clippers",
                                "price": 1.23
                            },
                            {
                                "name": "Memphis Grizzlies",
                                "price": 4.4
                            }
                        ]
                    },
                    {
                        "key": "spreads",
                        "last_update": "2024-02-23T13:40:36Z",
                        "outcomes": [
                            {
                                "name": "Los Angeles Clippers",
                                "price": 1.91,
                                "point": -9.5
                            },
                            {
                                "name": "Memphis Grizzlies",
                                "price": 1.91,
                                "point": 9.5
                            }
                        ]
                    },
                    {
                        "key": "totals",
                        "last_update": "2024-02-23T13:40:36Z",
                        "outcomes": [
                            {
                                "name": "Over",
                                "price": 1.89,
                                "point": 223.0
                            },
                            {
                                "name": "Under",
                                "price": 1.92,
                                "point": 223.0
                            }
                        ]
                    }
                ]
            },
            {
                "key": "unibet_us",
                "title": "Unibet",
                "last_update": "2024-02-23T13:40:36Z",
                "markets": [
                    {
                        "key": "h2h",
                        "last_update": "2024-02-23T13:40:36Z",
                        "outcomes": [
                            {
                                "name": "Los Angeles Clippers",
                                "price": 1.23
                            },
                            {
                                "name": "Memphis Grizzlies",
                                "price": 4.4
                            }
                        ]
                    },
                    {
                        "key": "spreads",
                        "last_update": "2024-02-23T13:40:36Z",
                        "outcomes": [
                            {
                                "name": "Los Angeles Clippers",
                                "price": 1.91,
                                "point": -9.5
                            },
                            {
                                "name": "Memphis Grizzlies",
                                "price": 1.91,
                                "point": 9.5
                            }
                        ]
                    },
                    {
                        "key": "totals",
                        "last_update": "2024-02-23T13:40:36Z",
                        "outcomes": [
                            {
                                "name": "Over",
                                "price": 1.89,
                                "point": 223.0
                            },
                            {
                                "name": "Under",
                                "price": 1.92,
                                "point": 223.0
                            }
                        ]
                    }
                ]
            },
            {
                "key": "williamhill_us",
                "title": "Caesars",
                "last_update": "2024-02-23T13:38:20Z",
                "markets": [
                    {
                        "key": "h2h",
                        "last_update": "2024-02-23T13:38:20Z",
                        "outcomes": [
                            {
                                "name": "Los Angeles Clippers",
                                "price": 1.23
                            },
                            {
                                "name": "Memphis Grizzlies",
                                "price": 4.35
                            }
                        ]
                    },
                    {
                        "key": "spreads",
                        "last_update": "2024-02-23T13:38:20Z",
                        "outcomes": [
                            {
                                "name": "Los Angeles Clippers",
                                "price": 1.91,
                                "point": -9.0
                            },
                            {
                                "name": "Memphis Grizzlies",
                                "price": 1.91,
                                "point": 9.0
                            }
                        ]
                    },
                    {
                        "key": "totals",
                        "last_update": "2024-02-23T13:38:20Z",
                        "outcomes": [
                            {
                                "name": "Over",
                                "price": 1.91,
                                "point": 222.5
                            },
                            {
                                "name": "Under",
                                "price": 1.91,
                                "point": 222.5
                            }
                        ]
                    }
                ]
            },
            {
                "key": "bovada",
                "title": "Bovada",
                "last_update": "2024-02-23T13:41:03Z",
                "markets": [
                    {
                        "key": "h2h",
                        "last_update": "2024-02-23T13:41:03Z",
                        "outcomes": [
                            {
                                "name": "Los Angeles Clippers",
                                "price": 1.24
                            },
                            {
                                "name": "Memphis Grizzlies",
                                "price": 4.15
                            }
                        ]
                    },
                    {
                        "key": "spreads",
                        "last_update": "2024-02-23T13:41:03Z",
                        "outcomes": [
                            {
                                "name": "Los Angeles Clippers",
                                "price": 1.91,
                                "point": -9.0
                            },
                            {
                                "name": "Memphis Grizzlies",
                                "price": 1.91,
                                "point": 9.0
                            }
                        ]
                    },
                    {
                        "key": "totals",
                        "last_update": "2024-02-23T13:41:03Z",
                        "outcomes": [
                            {
                                "name": "Over",
                                "price": 1.91,
                                "point": 222.0
                            },
                            {
                                "name": "Under",
                                "price": 1.91,
                                "point": 222.0
                            }
                        ]
                    }
                ]
            },
            {
                "key": "lowvig",
                "title": "LowVig.ag",
                "last_update": "2024-02-23T13:41:04Z",
                "markets": [
                    {
                        "key": "h2h",
                        "last_update": "2024-02-23T13:41:04Z",
                        "outcomes": [
                            {
                                "name": "Los Angeles Clippers",
                                "price": 1.25
                            },
                            {
                                "name": "Memphis Grizzlies",
                                "price": 4.25
                            }
                        ]
                    },
                    {
                        "key": "spreads",
                        "last_update": "2024-02-23T13:41:04Z",
                        "outcomes": [
                            {
                                "name": "Los Angeles Clippers",
                                "price": 1.94,
                                "point": -9.0
                            },
                            {
                                "name": "Memphis Grizzlies",
                                "price": 1.94,
                                "point": 9.0
                            }
                        ]
                    },
                    {
                        "key": "totals",
                        "last_update": "2024-02-23T13:41:04Z",
                        "outcomes": [
                            {
                                "name": "Over",
                                "price": 1.94,
                                "point": 222.5
                            },
                            {
                                "name": "Under",
                                "price": 1.94,
                                "point": 222.5
                            }
                        ]
                    }
                ]
            },
            {
                "key": "betonlineag",
                "title": "BetOnline.ag",
                "last_update": "2024-02-23T13:40:35Z",
                "markets": [
                    {
                        "key": "h2h",
                        "last_update": "2024-02-23T13:40:35Z",
                        "outcomes": [
                            {
                                "name": "Los Angeles Clippers",
                                "price": 1.25
                            },
                            {
                                "name": "Memphis Grizzlies",
                                "price": 4.25
                            }
                        ]
                    },
                    {
                        "key": "spreads",
                        "last_update": "2024-02-23T13:40:35Z",
                        "outcomes": [
                            {
                                "name": "Los Angeles Clippers",
                                "price": 1.91,
                                "point": -9.0
                            },
                            {
                                "name": "Memphis Grizzlies",
                                "price": 1.91,
                                "point": 9.0
                            }
                        ]
                    },
                    {
                        "key": "totals",
                        "last_update": "2024-02-23T13:40:35Z",
                        "outcomes": [
                            {
                                "name": "Over",
                                "price": 1.91,
                                "point": 222.5
                            },
                            {
                                "name": "Under",
                                "price": 1.91,
                                "point": 222.5
                            }
                        ]
                    }
                ]
            },
            {
                "key": "betus",
                "title": "BetUS",
                "last_update": "2024-02-23T13:40:36Z",
                "markets": [
                    {
                        "key": "h2h",
                        "last_update": "2024-02-23T13:40:36Z",
                        "outcomes": [
                            {
                                "name": "Los Angeles Clippers",
                                "price": 1.25
                            },
                            {
                                "name": "Memphis Grizzlies",
                                "price": 4.25
                            }
                        ]
                    },
                    {
                        "key": "spreads",
                        "last_update": "2024-02-23T13:40:36Z",
                        "outcomes": [
                            {
                                "name": "Los Angeles Clippers",
                                "price": 1.91,
                                "point": -9.0
                            },
                            {
                                "name": "Memphis Grizzlies",
                                "price": 1.91,
                                "point": 9.0
                            }
                        ]
                    },
                    {
                        "key": "totals",
                        "last_update": "2024-02-23T13:40:36Z",
                        "outcomes": [
                            {
                                "name": "Over",
                                "price": 1.91,
                                "point": 222.5
                            },
                            {
                                "name": "Under",
                                "price": 1.91,
                                "point": 222.5
                            }
                        ]
                    }
                ]
            }
        ]
    },
    {
        "id": "98d566947c547e8bb26052248aa9886a",
        "sport_key": "basketball_nba",
        "sport_title": "NBA",
        "commence_time": "2024-02-24T01:10:00Z",
        "home_team": "New Orleans Pelicans",
        "away_team": "Miami Heat",
        "bookmakers": [
            {
                "key": "draftkings",
                "title": "DraftKings",
                "last_update": "2024-02-23T13:40:35Z",
                "markets": [
                    {
                        "key": "h2h",
                        "last_update": "2024-02-23T13:40:35Z",
                        "outcomes": [
                            {
                                "name": "Miami Heat",
                                "price": 2.3
                            },
                            {
                                "name": "New Orleans Pelicans",
                                "price": 1.65
                            }
                        ]
                    },
                    {
                        "key": "spreads",
                        "last_update": "2024-02-23T13:40:35Z",
                        "outcomes": [
                            {
                                "name": "Miami Heat",
                                "price": 1.91,
                                "point": 3.5
                            },
                            {
                                "name": "New Orleans Pelicans",
                                "price": 1.91,
                                "point": -3.5
                            }
                        ]
                    },
                    {
                        "key": "totals",
                        "last_update": "2024-02-23T13:40:35Z",
                        "outcomes": [
                            {
                                "name": "Over",
                                "price": 1.91,
                                "point": 220.0
                            },
                            {
                                "name": "Under",
                                "price": 1.91,
                                "point": 220.0
                            }
                        ]
                    }
                ]
            },
            {
                "key": "wynnbet",
                "title": "WynnBET",
                "last_update": "2024-02-23T13:41:03Z",
                "markets": [
                    {
                        "key": "h2h",
                        "last_update": "2024-02-23T13:41:03Z",
                        "outcomes": [
                            {
                                "name": "Miami Heat",
                                "price": 2.3
                            },
                            {
                                "name": "New Orleans Pelicans",
                                "price": 1.66
                            }
                        ]
                    },
                    {
                        "key": "spreads",
                        "last_update": "2024-02-23T13:41:03Z",
                        "outcomes": [
                            {
                                "name": "Miami Heat",
                                "price": 1.91,
                                "point": 3.5
                            },
                            {
                                "name": "New Orleans Pelicans",
                                "price": 1.91,
                                "point": -3.5
                            }
                        ]
                    },
                    {
                        "key": "totals",
                        "last_update": "2024-02-23T13:41:03Z",
                        "outcomes": [
                            {
                                "name": "Over",
                                "price": 1.91,
                                "point": 220.5
                            },
                            {
                                "name": "Under",
                                "price": 1.91,
                                "point": 220.5
                            }
                        ]
                    }
                ]
            },
            {
                "key": "mybookieag",
                "title": "MyBookie.ag",
                "last_update": "2024-02-23T13:40:35Z",
                "markets": [
                    {
                        "key": "h2h",
                        "last_update": "2024-02-23T13:40:35Z",
                        "outcomes": [
                            {
                                "name": "Miami Heat",
                                "price": 2.35
                            },
                            {
                                "name": "New Orleans Pelicans",
                                "price": 1.65
                            }
                        ]
                    },
                    {
                        "key": "spreads",
                        "last_update": "2024-02-23T13:40:35Z",
                        "outcomes": [
                            {
                                "name": "Miami Heat",
                                "price": 1.91,
                                "point": 3.5
                            },
                            {
                                "name": "New Orleans Pelicans",
                                "price": 1.91,
                                "point": -3.5
                            }
                        ]
                    },
                    {
                        "key": "totals",
                        "last_update": "2024-02-23T13:40:35Z",
                        "outcomes": [
                            {
                                "name": "Over",
                                "price": 1.91,
                                "point": 220.5
                            },
                            {
                                "name": "Under",
                                "price": 1.91,
                                "point": 220.5
                            }
                        ]
                    }
                ]
            },
            {
                "key": "fanduel",
                "title": "FanDuel",
                "last_update": "2024-02-23T13:40:06Z",
                "markets": [
                    {
                        "key": "h2h",
                        "last_update": "2024-02-23T13:40:06Z",
                        "outcomes": [
                            {
                                "name": "Miami Heat",
                                "price": 2.32
                            },
                            {
                                "name": "New Orleans Pelicans",
                                "price": 1.64
                            }
                        ]
                    },
                    {
                        "key": "spreads",
                        "last_update": "2024-02-23T13:40:06Z",
                        "outcomes": [
                            {
                                "name": "Miami Heat",
                                "price": 1.89,
                                "point": 3.5
                            },
                            {
                                "name": "New Orleans Pelicans",
                                "price": 1.93,
                                "point": -3.5
                            }
                        ]
                    },
                    {
                        "key": "totals",
                        "last_update": "2024-02-23T13:40:06Z",
                        "outcomes": [
                            {
                                "name": "Over",
                                "price": 1.91,
                                "point": 220.0
                            },
                            {
                                "name": "Under",
                                "price": 1.91,
                                "point": 220.0
                            }
                        ]
                    }
                ]
            },
            {
                "key": "pointsbetus",
                "title": "PointsBet (US)",
                "last_update": "2024-02-23T13:40:35Z",
                "markets": [
                    {
                        "key": "h2h",
                        "last_update": "2024-02-23T13:40:35Z",
                        "outcomes": [
                            {
                                "name": "Miami Heat",
                                "price": 2.3
                            },
                            {
                                "name": "New Orleans Pelicans",
                                "price": 1.62
                            }
                        ]
                    },
                    {
                        "key": "spreads",
                        "last_update": "2024-02-23T13:40:35Z",
                        "outcomes": [
                            {
                                "name": "Miami Heat",
                                "price": 1.91,
                                "point": 3.5
                            },
                            {
                                "name": "New Orleans Pelicans",
                                "price": 1.91,
                                "point": -3.5
                            }
                        ]
                    },
                    {
                        "key": "totals",
                        "last_update": "2024-02-23T13:40:35Z",
                        "outcomes": [
                            {
                                "name": "Over",
                                "price": 1.91,
                                "point": 220.0
                            },
                            {
                                "name": "Under",
                                "price": 1.91,
                                "point": 220.0
                            }
                        ]
                    }
                ]
            },
            {
                "key": "betmgm",
                "title": "BetMGM",
                "last_update": "2024-02-23T13:38:20Z",
                "markets": [
                    {
                        "key": "h2h",
                        "last_update": "2024-02-23T13:38:20Z",
                        "outcomes": [
                            {
                                "name": "Miami Heat",
                                "price": 2.35
                            },
                            {
                                "name": "New Orleans Pelicans",
                                "price": 1.62
                            }
                        ]
                    },
                    {
                        "key": "spreads",
                        "last_update": "2024-02-23T13:38:20Z",
                        "outcomes": [
                            {
                                "name": "Miami Heat",
                                "price": 1.91,
                                "point": 3.5
                            },
                            {
                                "name": "New Orleans Pelicans",
                                "price": 1.91,
                                "point": -3.5
                            }
                        ]
                    },
                    {
                        "key": "totals",
                        "last_update": "2024-02-23T13:38:20Z",
                        "outcomes": [
                            {
                                "name": "Over",
                                "price": 1.91,
                                "point": 220.5
                            },
                            {
                                "name": "Under",
                                "price": 1.91,
                                "point": 220.5
                            }
                        ]
                    }
                ]
            },
            {
                "key": "unibet_us",
                "title": "Unibet",
                "last_update": "2024-02-23T13:40:36Z",
                "markets": [
                    {
                        "key": "h2h",
                        "last_update": "2024-02-23T13:40:36Z",
                        "outcomes": [
                            {
                                "name": "Miami Heat",
                                "price": 2.43
                            },
                            {
                                "name": "New Orleans Pelicans",
                                "price": 1.6
                            }
                        ]
                    },
                    {
                        "key": "spreads",
                        "last_update": "2024-02-23T13:40:36Z",
                        "outcomes": [
                            {
                                "name": "Miami Heat",
                                "price": 1.93,
                                "point": 3.5
                            },
                            {
                                "name": "New Orleans Pelicans",
                                "price": 1.88,
                                "point": -3.5
                            }
                        ]
                    },
                    {
                        "key": "totals",
                        "last_update": "2024-02-23T13:40:36Z",
                        "outcomes": [
                            {
                                "name": "Over",
                                "price": 1.89,
                                "point": 220.5
                            },
                            {
                                "name": "Under",
                                "price": 1.92,
                                "point": 220.5
                            }
                        ]
                    }
                ]
            },
            {
                "key": "betrivers",
                "title": "BetRivers",
                "last_update": "2024-02-23T13:40:36Z",
                "markets": [
                    {
                        "key": "h2h",
                        "last_update": "2024-02-23T13:40:36Z",
                        "outcomes": [
                            {
                                "name": "Miami Heat",
                                "price": 2.43
                            },
                            {
                                "name": "New Orleans Pelicans",
                                "price": 1.6
                            }
                        ]
                    },
                    {
                        "key": "spreads",
                        "last_update": "2024-02-23T13:40:36Z",
                        "outcomes": [
                            {
                                "name": "Miami Heat",
                                "price": 1.93,
                                "point": 3.5
                            },
                            {
                                "name": "New Orleans Pelicans",
                                "price": 1.88,
                                "point": -3.5
                            }
                        ]
                    },
                    {
                        "key": "totals",
                        "last_update": "2024-02-23T13:40:36Z",
                        "outcomes": [
                            {
                                "name": "Over",
                                "price": 1.89,
                                "point": 220.5
                            },
                            {
                                "name": "Under",
                                "price": 1.92,
                                "point": 220.5
                            }
                        ]
                    }
                ]
            },
            {
                "key": "williamhill_us",
                "title": "Caesars",
                "last_update": "2024-02-23T13:38:20Z",
                "markets": [
                    {
                        "key": "h2h",
                        "last_update": "2024-02-23T13:38:20Z",
                        "outcomes": [
                            {
                                "name": "Miami Heat",
                                "price": 2.4
                            },
                            {
                                "name": "New Orleans Pelicans",
                                "price": 1.61
                            }
                        ]
                    },
                    {
                        "key": "spreads",
                        "last_update": "2024-02-23T13:38:20Z",
                        "outcomes": [
                            {
                                "name": "Miami Heat",
                                "price": 1.91,
                                "point": 3.5
                            },
                            {
                                "name": "New Orleans Pelicans",
                                "price": 1.91,
                                "point": -3.5
                            }
                        ]
                    },
                    {
                        "key": "totals",
                        "last_update": "2024-02-23T13:38:20Z",
                        "outcomes": [
                            {
                                "name": "Over",
                                "price": 1.91,
                                "point": 220.0
                            },
                            {
                                "name": "Under",
                                "price": 1.91,
                                "point": 220.0
                            }
                        ]
                    }
                ]
            },
            {
                "key": "bovada",
                "title": "Bovada",
                "last_update": "2024-02-23T13:41:03Z",
                "markets": [
                    {
                        "key": "h2h",
                        "last_update": "2024-02-23T13:41:03Z",
                        "outcomes": [
                            {
                                "name": "Miami Heat",
                                "price": 2.3
                            },
                            {
                                "name": "New Orleans Pelicans",
                                "price": 1.67
                            }
                        ]
                    },
                    {
                        "key": "spreads",
                        "last_update": "2024-02-23T13:41:03Z",
                        "outcomes": [
                            {
                                "name": "Miami Heat",
                                "price": 1.87,
                                "point": 3.5
                            },
                            {
                                "name": "New Orleans Pelicans",
                                "price": 1.95,
                                "point": -3.5
                            }
                        ]
                    },
                    {
                        "key": "totals",
                        "last_update": "2024-02-23T13:41:03Z",
                        "outcomes": [
                            {
                                "name": "Over",
                                "price": 1.91,
                                "point": 220.0
                            },
                            {
                                "name": "Under",
                                "price": 1.91,
                                "point": 220.0
                            }
                        ]
                    }
                ]
            },
            {
                "key": "betonlineag",
                "title": "BetOnline.ag",
                "last_update": "2024-02-23T13:40:35Z",
                "markets": [
                    {
                        "key": "h2h",
                        "last_update": "2024-02-23T13:40:35Z",
                        "outcomes": [
                            {
                                "name": "Miami Heat",
                                "price": 2.33
                            },
                            {
                                "name": "New Orleans Pelicans",
                                "price": 1.65
                            }
                        ]
                    },
                    {
                        "key": "spreads",
                        "last_update": "2024-02-23T13:40:35Z",
                        "outcomes": [
                            {
                                "name": "Miami Heat",
                                "price": 1.88,
                                "point": 3.5
                            },
                            {
                                "name": "New Orleans Pelicans",
                                "price": 1.93,
                                "point": -3.5
                            }
                        ]
                    },
                    {
                        "key": "totals",
                        "last_update": "2024-02-23T13:40:35Z",
                        "outcomes": [
                            {
                                "name": "Over",
                                "price": 1.91,
                                "point": 220.0
                            },
                            {
                                "name": "Under",
                                "price": 1.91,
                                "point": 220.0
                            }
                        ]
                    }
                ]
            },
            {
                "key": "lowvig",
                "title": "LowVig.ag",
                "last_update": "2024-02-23T13:41:04Z",
                "markets": [
                    {
                        "key": "h2h",
                        "last_update": "2024-02-23T13:41:04Z",
                        "outcomes": [
                            {
                                "name": "Miami Heat",
                                "price": 2.33
                            },
                            {
                                "name": "New Orleans Pelicans",
                                "price": 1.65
                            }
                        ]
                    },
                    {
                        "key": "spreads",
                        "last_update": "2024-02-23T13:41:04Z",
                        "outcomes": [
                            {
                                "name": "Miami Heat",
                                "price": 1.92,
                                "point": 3.5
                            },
                            {
                                "name": "New Orleans Pelicans",
                                "price": 1.97,
                                "point": -3.5
                            }
                        ]
                    },
                    {
                        "key": "totals",
                        "last_update": "2024-02-23T13:41:04Z",
                        "outcomes": [
                            {
                                "name": "Over",
                                "price": 1.94,
                                "point": 220.0
                            },
                            {
                                "name": "Under",
                                "price": 1.94,
                                "point": 220.0
                            }
                        ]
                    }
                ]
            },
            {
                "key": "betus",
                "title": "BetUS",
                "last_update": "2024-02-23T13:40:36Z",
                "markets": [
                    {
                        "key": "h2h",
                        "last_update": "2024-02-23T13:40:36Z",
                        "outcomes": [
                            {
                                "name": "Miami Heat",
                                "price": 2.35
                            },
                            {
                                "name": "New Orleans Pelicans",
                                "price": 1.65
                            }
                        ]
                    },
                    {
                        "key": "spreads",
                        "last_update": "2024-02-23T13:40:36Z",
                        "outcomes": [
                            {
                                "name": "Miami Heat",
                                "price": 1.91,
                                "point": 3.5
                            },
                            {
                                "name": "New Orleans Pelicans",
                                "price": 1.91,
                                "point": -3.5
                            }
                        ]
                    },
                    {
                        "key": "totals",
                        "last_update": "2024-02-23T13:40:36Z",
                        "outcomes": [
                            {
                                "name": "Over",
                                "price": 1.91,
                                "point": 220.0
                            },
                            {
                                "name": "Under",
                                "price": 1.91,
                                "point": 220.0
                            }
                        ]
                    }
                ]
            }
        ]
    },
    {
        "id": "703e78f878fd29658600d9a1ca392817",
        "sport_key": "basketball_nba",
        "sport_title": "NBA",
        "commence_time": "2024-02-24T01:10:00Z",
        "home_team": "Oklahoma City Thunder",
        "away_team": "Washington Wizards",
        "bookmakers": [
            {
                "key": "draftkings",
                "title": "DraftKings",
                "last_update": "2024-02-23T13:40:35Z",
                "markets": [
                    {
                        "key": "h2h",
                        "last_update": "2024-02-23T13:40:35Z",
                        "outcomes": [
                            {
                                "name": "Oklahoma City Thunder",
                                "price": 1.07
                            },
                            {
                                "name": "Washington Wizards",
                                "price": 9.5
                            }
                        ]
                    },
                    {
                        "key": "spreads",
                        "last_update": "2024-02-23T13:40:35Z",
                        "outcomes": [
                            {
                                "name": "Oklahoma City Thunder",
                                "price": 1.95,
                                "point": -16.0
                            },
                            {
                                "name": "Washington Wizards",
                                "price": 1.87,
                                "point": 16.0
                            }
                        ]
                    },
                    {
                        "key": "totals",
                        "last_update": "2024-02-23T13:40:35Z",
                        "outcomes": [
                            {
                                "name": "Over",
                                "price": 1.89,
                                "point": 240.5
                            },
                            {
                                "name": "Under",
                                "price": 1.93,
                                "point": 240.5
                            }
                        ]
                    }
                ]
            },
            {
                "key": "lowvig",
                "title": "LowVig.ag",
                "last_update": "2024-02-23T13:41:04Z",
                "markets": [
                    {
                        "key": "h2h",
                        "last_update": "2024-02-23T13:41:04Z",
                        "outcomes": [
                            {
                                "name": "Oklahoma City Thunder",
                                "price": 1.07
                            },
                            {
                                "name": "Washington Wizards",
                                "price": 9.7
                            }
                        ]
                    },
                    {
                        "key": "spreads",
                        "last_update": "2024-02-23T13:41:04Z",
                        "outcomes": [
                            {
                                "name": "Oklahoma City Thunder",
                                "price": 1.94,
                                "point": -16.0
                            },
                            {
                                "name": "Washington Wizards",
                                "price": 1.94,
                                "point": 16.0
                            }
                        ]
                    },
                    {
                        "key": "totals",
                        "last_update": "2024-02-23T13:41:04Z",
                        "outcomes": [
                            {
                                "name": "Over",
                                "price": 1.94,
                                "point": 240.5
                            },
                            {
                                "name": "Under",
                                "price": 1.94,
                                "point": 240.5
                            }
                        ]
                    }
                ]
            },
            {
                "key": "williamhill_us",
                "title": "Caesars",
                "last_update": "2024-02-23T13:38:20Z",
                "markets": [
                    {
                        "key": "h2h",
                        "last_update": "2024-02-23T13:38:20Z",
                        "outcomes": [
                            {
                                "name": "Oklahoma City Thunder",
                                "price": 1.07
                            },
                            {
                                "name": "Washington Wizards",
                                "price": 9.0
                            }
                        ]
                    },
                    {
                        "key": "spreads",
                        "last_update": "2024-02-23T13:38:20Z",
                        "outcomes": [
                            {
                                "name": "Oklahoma City Thunder",
                                "price": 1.91,
                                "point": -15.5
                            },
                            {
                                "name": "Washington Wizards",
                                "price": 1.91,
                                "point": 15.5
                            }
                        ]
                    },
                    {
                        "key": "totals",
                        "last_update": "2024-02-23T13:38:20Z",
                        "outcomes": [
                            {
                                "name": "Over",
                                "price": 1.91,
                                "point": 240.5
                            },
                            {
                                "name": "Under",
                                "price": 1.91,
                                "point": 240.5
                            }
                        ]
                    }
                ]
            },
            {
                "key": "betonlineag",
                "title": "BetOnline.ag",
                "last_update": "2024-02-23T13:40:35Z",
                "markets": [
                    {
                        "key": "h2h",
                        "last_update": "2024-02-23T13:40:35Z",
                        "outcomes": [
                            {
                                "name": "Oklahoma City Thunder",
                                "price": 1.07
                            },
                            {
                                "name": "Washington Wizards",
                                "price": 9.7
                            }
                        ]
                    },
                    {
                        "key": "spreads",
                        "last_update": "2024-02-23T13:40:35Z",
                        "outcomes": [
                            {
                                "name": "Oklahoma City Thunder",
                                "price": 1.91,
                                "point": -16.0
                            },
                            {
                                "name": "Washington Wizards",
                                "price": 1.91,
                                "point": 16.0
                            }
                        ]
                    },
                    {
                        "key": "totals",
                        "last_update": "2024-02-23T13:40:35Z",
                        "outcomes": [
                            {
                                "name": "Over",
                                "price": 1.91,
                                "point": 240.5
                            },
                            {
                                "name": "Under",
                                "price": 1.91,
                                "point": 240.5
                            }
                        ]
                    }
                ]
            },
            {
                "key": "wynnbet",
                "title": "WynnBET",
                "last_update": "2024-02-23T13:41:03Z",
                "markets": [
                    {
                        "key": "h2h",
                        "last_update": "2024-02-23T13:41:03Z",
                        "outcomes": [
                            {
                                "name": "Oklahoma City Thunder",
                                "price": 1.07
                            },
                            {
                                "name": "Washington Wizards",
                                "price": 9.75
                            }
                        ]
                    },
                    {
                        "key": "spreads",
                        "last_update": "2024-02-23T13:41:03Z",
                        "outcomes": [
                            {
                                "name": "Oklahoma City Thunder",
                                "price": 1.91,
                                "point": -15.5
                            },
                            {
                                "name": "Washington Wizards",
                                "price": 1.91,
                                "point": 15.5
                            }
                        ]
                    },
                    {
                        "key": "totals",
                        "last_update": "2024-02-23T13:41:03Z",
                        "outcomes": [
                            {
                                "name": "Over",
                                "price": 1.91,
                                "point": 240.5
                            },
                            {
                                "name": "Under",
                                "price": 1.91,
                                "point": 240.5
                            }
                        ]
                    }
                ]
            },
            {
                "key": "pointsbetus",
                "title": "PointsBet (US)",
                "last_update": "2024-02-23T13:40:35Z",
                "markets": [
                    {
                        "key": "h2h",
                        "last_update": "2024-02-23T13:40:35Z",
                        "outcomes": [
                            {
                                "name": "Oklahoma City Thunder",
                                "price": 1.08
                            },
                            {
                                "name": "Washington Wizards",
                                "price": 9.0
                            }
                        ]
                    },
                    {
                        "key": "spreads",
                        "last_update": "2024-02-23T13:40:35Z",
                        "outcomes": [
                            {
                                "name": "Oklahoma City Thunder",
                                "price": 1.91,
                                "point": -15.5
                            },
                            {
                                "name": "Washington Wizards",
                                "price": 1.91,
                                "point": 15.5
                            }
                        ]
                    },
                    {
                        "key": "totals",
                        "last_update": "2024-02-23T13:40:35Z",
                        "outcomes": [
                            {
                                "name": "Over",
                                "price": 1.91,
                                "point": 240.5
                            },
                            {
                                "name": "Under",
                                "price": 1.91,
                                "point": 240.5
                            }
                        ]
                    }
                ]
            },
            {
                "key": "mybookieag",
                "title": "MyBookie.ag",
                "last_update": "2024-02-23T13:40:35Z",
                "markets": [
                    {
                        "key": "h2h",
                        "last_update": "2024-02-23T13:40:35Z",
                        "outcomes": [
                            {
                                "name": "Oklahoma City Thunder",
                                "price": 1.08
                            },
                            {
                                "name": "Washington Wizards",
                                "price": 7.75
                            }
                        ]
                    },
                    {
                        "key": "spreads",
                        "last_update": "2024-02-23T13:40:35Z",
                        "outcomes": [
                            {
                                "name": "Oklahoma City Thunder",
                                "price": 1.91,
                                "point": -15.5
                            },
                            {
                                "name": "Washington Wizards",
                                "price": 1.91,
                                "point": 15.5
                            }
                        ]
                    },
                    {
                        "key": "totals",
                        "last_update": "2024-02-23T13:40:35Z",
                        "outcomes": [
                            {
                                "name": "Over",
                                "price": 1.91,
                                "point": 241.0
                            },
                            {
                                "name": "Under",
                                "price": 1.91,
                                "point": 241.0
                            }
                        ]
                    }
                ]
            },
            {
                "key": "fanduel",
                "title": "FanDuel",
                "last_update": "2024-02-23T13:40:06Z",
                "markets": [
                    {
                        "key": "h2h",
                        "last_update": "2024-02-23T13:40:06Z",
                        "outcomes": [
                            {
                                "name": "Oklahoma City Thunder",
                                "price": 1.06
                            },
                            {
                                "name": "Washington Wizards",
                                "price": 10.0
                            }
                        ]
                    },
                    {
                        "key": "spreads",
                        "last_update": "2024-02-23T13:40:06Z",
                        "outcomes": [
                            {
                                "name": "Oklahoma City Thunder",
                                "price": 1.91,
                                "point": -15.5
                            },
                            {
                                "name": "Washington Wizards",
                                "price": 1.91,
                                "point": 15.5
                            }
                        ]
                    },
                    {
                        "key": "totals",
                        "last_update": "2024-02-23T13:40:06Z",
                        "outcomes": [
                            {
                                "name": "Over",
                                "price": 1.91,
                                "point": 240.5
                            },
                            {
                                "name": "Under",
                                "price": 1.91,
                                "point": 240.5
                            }
                        ]
                    }
                ]
            },
            {
                "key": "bovada",
                "title": "Bovada",
                "last_update": "2024-02-23T13:41:03Z",
                "markets": [
                    {
                        "key": "h2h",
                        "last_update": "2024-02-23T13:41:03Z",
                        "outcomes": [
                            {
                                "name": "Oklahoma City Thunder",
                                "price": 1.06
                            },
                            {
                                "name": "Washington Wizards",
                                "price": 9.0
                            }
                        ]
                    },
                    {
                        "key": "spreads",
                        "last_update": "2024-02-23T13:41:03Z",
                        "outcomes": [
                            {
                                "name": "Oklahoma City Thunder",
                                "price": 1.91,
                                "point": -15.5
                            },
                            {
                                "name": "Washington Wizards",
                                "price": 1.91,
                                "point": 15.5
                            }
                        ]
                    },
                    {
                        "key": "totals",
                        "last_update": "2024-02-23T13:41:03Z",
                        "outcomes": [
                            {
                                "name": "Over",
                                "price": 1.91,
                                "point": 241.0
                            },
                            {
                                "name": "Under",
                                "price": 1.91,
                                "point": 241.0
                            }
                        ]
                    }
                ]
            },
            {
                "key": "betmgm",
                "title": "BetMGM",
                "last_update": "2024-02-23T13:38:20Z",
                "markets": [
                    {
                        "key": "h2h",
                        "last_update": "2024-02-23T13:38:20Z",
                        "outcomes": [
                            {
                                "name": "Oklahoma City Thunder",
                                "price": 1.07
                            },
                            {
                                "name": "Washington Wizards",
                                "price": 9.25
                            }
                        ]
                    },
                    {
                        "key": "spreads",
                        "last_update": "2024-02-23T13:38:20Z",
                        "outcomes": [
                            {
                                "name": "Oklahoma City Thunder",
                                "price": 1.91,
                                "point": -15.5
                            },
                            {
                                "name": "Washington Wizards",
                                "price": 1.91,
                                "point": 15.5
                            }
                        ]
                    },
                    {
                        "key": "totals",
                        "last_update": "2024-02-23T13:38:20Z",
                        "outcomes": [
                            {
                                "name": "Over",
                                "price": 1.91,
                                "point": 240.5
                            },
                            {
                                "name": "Under",
                                "price": 1.91,
                                "point": 240.5
                            }
                        ]
                    }
                ]
            },
            {
                "key": "unibet_us",
                "title": "Unibet",
                "last_update": "2024-02-23T13:40:36Z",
                "markets": [
                    {
                        "key": "h2h",
                        "last_update": "2024-02-23T13:40:36Z",
                        "outcomes": [
                            {
                                "name": "Oklahoma City Thunder",
                                "price": 1.09
                            },
                            {
                                "name": "Washington Wizards",
                                "price": 8.0
                            }
                        ]
                    },
                    {
                        "key": "spreads",
                        "last_update": "2024-02-23T13:40:36Z",
                        "outcomes": [
                            {
                                "name": "Oklahoma City Thunder",
                                "price": 1.92,
                                "point": -15.5
                            },
                            {
                                "name": "Washington Wizards",
                                "price": 1.89,
                                "point": 15.5
                            }
                        ]
                    },
                    {
                        "key": "totals",
                        "last_update": "2024-02-23T13:40:36Z",
                        "outcomes": [
                            {
                                "name": "Over",
                                "price": 1.93,
                                "point": 241.0
                            },
                            {
                                "name": "Under",
                                "price": 1.88,
                                "point": 241.0
                            }
                        ]
                    }
                ]
            },
            {
                "key": "betrivers",
                "title": "BetRivers",
                "last_update": "2024-02-23T13:40:36Z",
                "markets": [
                    {
                        "key": "h2h",
                        "last_update": "2024-02-23T13:40:36Z",
                        "outcomes": [
                            {
                                "name": "Oklahoma City Thunder",
                                "price": 1.09
                            },
                            {
                                "name": "Washington Wizards",
                                "price": 8.0
                            }
                        ]
                    },
                    {
                        "key": "spreads",
                        "last_update": "2024-02-23T13:40:36Z",
                        "outcomes": [
                            {
                                "name": "Oklahoma City Thunder",
                                "price": 1.92,
                                "point": -15.5
                            },
                            {
                                "name": "Washington Wizards",
                                "price": 1.89,
                                "point": 15.5
                            }
                        ]
                    },
                    {
                        "key": "totals",
                        "last_update": "2024-02-23T13:40:36Z",
                        "outcomes": [
                            {
                                "name": "Over",
                                "price": 1.88,
                                "point": 240.5
                            },
                            {
                                "name": "Under",
                                "price": 1.93,
                                "point": 240.5
                            }
                        ]
                    }
                ]
            },
            {
                "key": "betus",
                "title": "BetUS",
                "last_update": "2024-02-23T13:40:36Z",
                "markets": [
                    {
                        "key": "h2h",
                        "last_update": "2024-02-23T13:40:36Z",
                        "outcomes": [
                            {
                                "name": "Oklahoma City Thunder",
                                "price": 1.07
                            },
                            {
                                "name": "Washington Wizards",
                                "price": 9.2
                            }
                        ]
                    },
                    {
                        "key": "spreads",
                        "last_update": "2024-02-23T13:40:36Z",
                        "outcomes": [
                            {
                                "name": "Oklahoma City Thunder",
                                "price": 1.91,
                                "point": -16.0
                            },
                            {
                                "name": "Washington Wizards",
                                "price": 1.91,
                                "point": 16.0
                            }
                        ]
                    },
                    {
                        "key": "totals",
                        "last_update": "2024-02-23T13:40:36Z",
                        "outcomes": [
                            {
                                "name": "Over",
                                "price": 1.91,
                                "point": 241.0
                            },
                            {
                                "name": "Under",
                                "price": 1.91,
                                "point": 241.0
                            }
                        ]
                    }
                ]
            }
        ]
    },
    {
        "id": "8665e61d2754ea047780ecda1705cf09",
        "sport_key": "basketball_nba",
        "sport_title": "NBA",
        "commence_time": "2024-02-24T03:10:00Z",
        "home_team": "Golden State Warriors",
        "away_team": "Charlotte Hornets",
        "bookmakers": [
            {
                "key": "draftkings",
                "title": "DraftKings",
                "last_update": "2024-02-23T13:40:35Z",
                "markets": [
                    {
                        "key": "h2h",
                        "last_update": "2024-02-23T13:40:35Z",
                        "outcomes": [
                            {
                                "name": "Charlotte Hornets",
                                "price": 7.0
                            },
                            {
                                "name": "Golden State Warriors",
                                "price": 1.11
                            }
                        ]
                    },
                    {
                        "key": "spreads",
                        "last_update": "2024-02-23T13:40:35Z",
                        "outcomes": [
                            {
                                "name": "Charlotte Hornets",
                                "price": 1.91,
                                "point": 13.0
                            },
                            {
                                "name": "Golden State Warriors",
                                "price": 1.91,
                                "point": -13.0
                            }
                        ]
                    },
                    {
                        "key": "totals",
                        "last_update": "2024-02-23T13:40:35Z",
                        "outcomes": [
                            {
                                "name": "Over",
                                "price": 1.93,
                                "point": 228.5
                            },
                            {
                                "name": "Under",
                                "price": 1.89,
                                "point": 228.5
                            }
                        ]
                    }
                ]
            },
            {
                "key": "wynnbet",
                "title": "WynnBET",
                "last_update": "2024-02-23T13:41:03Z",
                "markets": [
                    {
                        "key": "h2h",
                        "last_update": "2024-02-23T13:41:03Z",
                        "outcomes": [
                            {
                                "name": "Charlotte Hornets",
                                "price": 7.75
                            },
                            {
                                "name": "Golden State Warriors",
                                "price": 1.1
                            }
                        ]
                    },
                    {
                        "key": "spreads",
                        "last_update": "2024-02-23T13:41:03Z",
                        "outcomes": [
                            {
                                "name": "Charlotte Hornets",
                                "price": 1.91,
                                "point": 13.0
                            },
                            {
                                "name": "Golden State Warriors",
                                "price": 1.91,
                                "point": -13.0
                            }
                        ]
                    },
                    {
                        "key": "totals",
                        "last_update": "2024-02-23T13:41:03Z",
                        "outcomes": [
                            {
                                "name": "Over",
                                "price": 1.91,
                                "point": 228.5
                            },
                            {
                                "name": "Under",
                                "price": 1.91,
                                "point": 228.5
                            }
                        ]
                    }
                ]
            },
            {
                "key": "mybookieag",
                "title": "MyBookie.ag",
                "last_update": "2024-02-23T13:40:35Z",
                "markets": [
                    {
                        "key": "h2h",
                        "last_update": "2024-02-23T13:40:35Z",
                        "outcomes": [
                            {
                                "name": "Charlotte Hornets",
                                "price": 6.75
                            },
                            {
                                "name": "Golden State Warriors",
                                "price": 1.11
                            }
                        ]
                    },
                    {
                        "key": "spreads",
                        "last_update": "2024-02-23T13:40:35Z",
                        "outcomes": [
                            {
                                "name": "Charlotte Hornets",
                                "price": 1.91,
                                "point": 13.0
                            },
                            {
                                "name": "Golden State Warriors",
                                "price": 1.91,
                                "point": -13.0
                            }
                        ]
                    },
                    {
                        "key": "totals",
                        "last_update": "2024-02-23T13:40:35Z",
                        "outcomes": [
                            {
                                "name": "Over",
                                "price": 1.91,
                                "point": 228.5
                            },
                            {
                                "name": "Under",
                                "price": 1.91,
                                "point": 228.5
                            }
                        ]
                    }
                ]
            },
            {
                "key": "fanduel",
                "title": "FanDuel",
                "last_update": "2024-02-23T13:40:06Z",
                "markets": [
                    {
                        "key": "h2h",
                        "last_update": "2024-02-23T13:40:06Z",
                        "outcomes": [
                            {
                                "name": "Charlotte Hornets",
                                "price": 6.7
                            },
                            {
                                "name": "Golden State Warriors",
                                "price": 1.12
                            }
                        ]
                    },
                    {
                        "key": "spreads",
                        "last_update": "2024-02-23T13:40:06Z",
                        "outcomes": [
                            {
                                "name": "Charlotte Hornets",
                                "price": 1.91,
                                "point": 13.0
                            },
                            {
                                "name": "Golden State Warriors",
                                "price": 1.91,
                                "point": -13.0
                            }
                        ]
                    },
                    {
                        "key": "totals",
                        "last_update": "2024-02-23T13:40:06Z",
                        "outcomes": [
                            {
                                "name": "Over",
                                "price": 1.91,
                                "point": 228.5
                            },
                            {
                                "name": "Under",
                                "price": 1.91,
                                "point": 228.5
                            }
                        ]
                    }
                ]
            },
            {
                "key": "pointsbetus",
                "title": "PointsBet (US)",
                "last_update": "2024-02-23T13:40:35Z",
                "markets": [
                    {
                        "key": "h2h",
                        "last_update": "2024-02-23T13:40:35Z",
                        "outcomes": [
                            {
                                "name": "Charlotte Hornets",
                                "price": 7.5
                            },
                            {
                                "name": "Golden State Warriors",
                                "price": 1.1
                            }
                        ]
                    },
                    {
                        "key": "spreads",
                        "last_update": "2024-02-23T13:40:35Z",
                        "outcomes": [
                            {
                                "name": "Charlotte Hornets",
                                "price": 1.91,
                                "point": 13.0
                            },
                            {
                                "name": "Golden State Warriors",
                                "price": 1.91,
                                "point": -13.0
                            }
                        ]
                    },
                    {
                        "key": "totals",
                        "last_update": "2024-02-23T13:40:35Z",
                        "outcomes": [
                            {
                                "name": "Over",
                                "price": 1.91,
                                "point": 229.0
                            },
                            {
                                "name": "Under",
                                "price": 1.91,
                                "point": 229.0
                            }
                        ]
                    }
                ]
            },
            {
                "key": "betmgm",
                "title": "BetMGM",
                "last_update": "2024-02-23T13:38:20Z",
                "markets": [
                    {
                        "key": "h2h",
                        "last_update": "2024-02-23T13:38:20Z",
                        "outcomes": [
                            {
                                "name": "Charlotte Hornets",
                                "price": 7.25
                            },
                            {
                                "name": "Golden State Warriors",
                                "price": 1.1
                            }
                        ]
                    },
                    {
                        "key": "spreads",
                        "last_update": "2024-02-23T13:38:20Z",
                        "outcomes": [
                            {
                                "name": "Charlotte Hornets",
                                "price": 1.95,
                                "point": 12.5
                            },
                            {
                                "name": "Golden State Warriors",
                                "price": 1.87,
                                "point": -12.5
                            }
                        ]
                    },
                    {
                        "key": "totals",
                        "last_update": "2024-02-23T13:38:20Z",
                        "outcomes": [
                            {
                                "name": "Over",
                                "price": 1.91,
                                "point": 228.5
                            },
                            {
                                "name": "Under",
                                "price": 1.91,
                                "point": 228.5
                            }
                        ]
                    }
                ]
            },
            {
                "key": "unibet_us",
                "title": "Unibet",
                "last_update": "2024-02-23T13:40:36Z",
                "markets": [
                    {
                        "key": "h2h",
                        "last_update": "2024-02-23T13:40:36Z",
                        "outcomes": [
                            {
                                "name": "Charlotte Hornets",
                                "price": 6.75
                            },
                            {
                                "name": "Golden State Warriors",
                                "price": 1.12
                            }
                        ]
                    },
                    {
                        "key": "spreads",
                        "last_update": "2024-02-23T13:40:36Z",
                        "outcomes": [
                            {
                                "name": "Charlotte Hornets",
                                "price": 1.91,
                                "point": 13.0
                            },
                            {
                                "name": "Golden State Warriors",
                                "price": 1.91,
                                "point": -13.0
                            }
                        ]
                    },
                    {
                        "key": "totals",
                        "last_update": "2024-02-23T13:40:36Z",
                        "outcomes": [
                            {
                                "name": "Over",
                                "price": 1.88,
                                "point": 228.0
                            },
                            {
                                "name": "Under",
                                "price": 1.93,
                                "point": 228.0
                            }
                        ]
                    }
                ]
            },
            {
                "key": "betrivers",
                "title": "BetRivers",
                "last_update": "2024-02-23T13:40:36Z",
                "markets": [
                    {
                        "key": "h2h",
                        "last_update": "2024-02-23T13:40:36Z",
                        "outcomes": [
                            {
                                "name": "Charlotte Hornets",
                                "price": 6.75
                            },
                            {
                                "name": "Golden State Warriors",
                                "price": 1.12
                            }
                        ]
                    },
                    {
                        "key": "spreads",
                        "last_update": "2024-02-23T13:40:36Z",
                        "outcomes": [
                            {
                                "name": "Charlotte Hornets",
                                "price": 1.91,
                                "point": 13.0
                            },
                            {
                                "name": "Golden State Warriors",
                                "price": 1.91,
                                "point": -13.0
                            }
                        ]
                    },
                    {
                        "key": "totals",
                        "last_update": "2024-02-23T13:40:36Z",
                        "outcomes": [
                            {
                                "name": "Over",
                                "price": 1.88,
                                "point": 228.0
                            },
                            {
                                "name": "Under",
                                "price": 1.93,
                                "point": 228.0
                            }
                        ]
                    }
                ]
            },
            {
                "key": "williamhill_us",
                "title": "Caesars",
                "last_update": "2024-02-23T13:38:20Z",
                "markets": [
                    {
                        "key": "h2h",
                        "last_update": "2024-02-23T13:38:20Z",
                        "outcomes": [
                            {
                                "name": "Charlotte Hornets",
                                "price": 7.5
                            },
                            {
                                "name": "Golden State Warriors",
                                "price": 1.1
                            }
                        ]
                    },
                    {
                        "key": "spreads",
                        "last_update": "2024-02-23T13:38:20Z",
                        "outcomes": [
                            {
                                "name": "Charlotte Hornets",
                                "price": 1.91,
                                "point": 13.0
                            },
                            {
                                "name": "Golden State Warriors",
                                "price": 1.91,
                                "point": -13.0
                            }
                        ]
                    },
                    {
                        "key": "totals",
                        "last_update": "2024-02-23T13:38:20Z",
                        "outcomes": [
                            {
                                "name": "Over",
                                "price": 1.91,
                                "point": 228.5
                            },
                            {
                                "name": "Under",
                                "price": 1.91,
                                "point": 228.5
                            }
                        ]
                    }
                ]
            },
            {
                "key": "bovada",
                "title": "Bovada",
                "last_update": "2024-02-23T13:41:03Z",
                "markets": [
                    {
                        "key": "h2h",
                        "last_update": "2024-02-23T13:41:03Z",
                        "outcomes": [
                            {
                                "name": "Charlotte Hornets",
                                "price": 6.75
                            },
                            {
                                "name": "Golden State Warriors",
                                "price": 1.11
                            }
                        ]
                    },
                    {
                        "key": "spreads",
                        "last_update": "2024-02-23T13:41:03Z",
                        "outcomes": [
                            {
                                "name": "Charlotte Hornets",
                                "price": 1.91,
                                "point": 13.0
                            },
                            {
                                "name": "Golden State Warriors",
                                "price": 1.91,
                                "point": -13.0
                            }
                        ]
                    },
                    {
                        "key": "totals",
                        "last_update": "2024-02-23T13:41:03Z",
                        "outcomes": [
                            {
                                "name": "Over",
                                "price": 1.95,
                                "point": 229.0
                            },
                            {
                                "name": "Under",
                                "price": 1.87,
                                "point": 229.0
                            }
                        ]
                    }
                ]
            },
            {
                "key": "lowvig",
                "title": "LowVig.ag",
                "last_update": "2024-02-23T13:41:04Z",
                "markets": [
                    {
                        "key": "h2h",
                        "last_update": "2024-02-23T13:41:04Z",
                        "outcomes": [
                            {
                                "name": "Charlotte Hornets",
                                "price": 7.4
                            },
                            {
                                "name": "Golden State Warriors",
                                "price": 1.11
                            }
                        ]
                    },
                    {
                        "key": "spreads",
                        "last_update": "2024-02-23T13:41:04Z",
                        "outcomes": [
                            {
                                "name": "Charlotte Hornets",
                                "price": 1.94,
                                "point": 13.0
                            },
                            {
                                "name": "Golden State Warriors",
                                "price": 1.94,
                                "point": -13.0
                            }
                        ]
                    },
                    {
                        "key": "totals",
                        "last_update": "2024-02-23T13:41:04Z",
                        "outcomes": [
                            {
                                "name": "Over",
                                "price": 1.94,
                                "point": 228.5
                            },
                            {
                                "name": "Under",
                                "price": 1.94,
                                "point": 228.5
                            }
                        ]
                    }
                ]
            },
            {
                "key": "betonlineag",
                "title": "BetOnline.ag",
                "last_update": "2024-02-23T13:40:35Z",
                "markets": [
                    {
                        "key": "h2h",
                        "last_update": "2024-02-23T13:40:35Z",
                        "outcomes": [
                            {
                                "name": "Charlotte Hornets",
                                "price": 7.4
                            },
                            {
                                "name": "Golden State Warriors",
                                "price": 1.11
                            }
                        ]
                    },
                    {
                        "key": "spreads",
                        "last_update": "2024-02-23T13:40:35Z",
                        "outcomes": [
                            {
                                "name": "Charlotte Hornets",
                                "price": 1.91,
                                "point": 13.0
                            },
                            {
                                "name": "Golden State Warriors",
                                "price": 1.91,
                                "point": -13.0
                            }
                        ]
                    },
                    {
                        "key": "totals",
                        "last_update": "2024-02-23T13:40:35Z",
                        "outcomes": [
                            {
                                "name": "Over",
                                "price": 1.91,
                                "point": 228.5
                            },
                            {
                                "name": "Under",
                                "price": 1.91,
                                "point": 228.5
                            }
                        ]
                    }
                ]
            },
            {
                "key": "betus",
                "title": "BetUS",
                "last_update": "2024-02-23T13:40:36Z",
                "markets": [
                    {
                        "key": "h2h",
                        "last_update": "2024-02-23T13:40:36Z",
                        "outcomes": [
                            {
                                "name": "Charlotte Hornets",
                                "price": 7.0
                            },
                            {
                                "name": "Golden State Warriors",
                                "price": 1.11
                            }
                        ]
                    },
                    {
                        "key": "spreads",
                        "last_update": "2024-02-23T13:40:36Z",
                        "outcomes": [
                            {
                                "name": "Charlotte Hornets",
                                "price": 1.91,
                                "point": 13.0
                            },
                            {
                                "name": "Golden State Warriors",
                                "price": 1.91,
                                "point": -13.0
                            }
                        ]
                    },
                    {
                        "key": "totals",
                        "last_update": "2024-02-23T13:40:36Z",
                        "outcomes": [
                            {
                                "name": "Over",
                                "price": 1.91,
                                "point": 228.5
                            },
                            {
                                "name": "Under",
                                "price": 1.91,
                                "point": 228.5
                            }
                        ]
                    }
                ]
            }
        ]
    },
    {
        "id": "f2b4edb503dc693b7031c1230fa906c1",
        "sport_key": "basketball_nba",
        "sport_title": "NBA",
        "commence_time": "2024-02-24T03:10:00Z",
        "home_team": "Portland Trail Blazers",
        "away_team": "Denver Nuggets",
        "bookmakers": [
            {
                "key": "draftkings",
                "title": "DraftKings",
                "last_update": "2024-02-23T13:40:35Z",
                "markets": [
                    {
                        "key": "h2h",
                        "last_update": "2024-02-23T13:40:35Z",
                        "outcomes": [
                            {
                                "name": "Denver Nuggets",
                                "price": 1.23
                            },
                            {
                                "name": "Portland Trail Blazers",
                                "price": 4.4
                            }
                        ]
                    },
                    {
                        "key": "spreads",
                        "last_update": "2024-02-23T13:40:35Z",
                        "outcomes": [
                            {
                                "name": "Denver Nuggets",
                                "price": 1.91,
                                "point": -9.5
                            },
                            {
                                "name": "Portland Trail Blazers",
                                "price": 1.91,
                                "point": 9.5
                            }
                        ]
                    },
                    {
                        "key": "totals",
                        "last_update": "2024-02-23T13:40:35Z",
                        "outcomes": [
                            {
                                "name": "Over",
                                "price": 1.91,
                                "point": 218.5
                            },
                            {
                                "name": "Under",
                                "price": 1.91,
                                "point": 218.5
                            }
                        ]
                    }
                ]
            },
            {
                "key": "betonlineag",
                "title": "BetOnline.ag",
                "last_update": "2024-02-23T13:40:35Z",
                "markets": [
                    {
                        "key": "h2h",
                        "last_update": "2024-02-23T13:40:35Z",
                        "outcomes": [
                            {
                                "name": "Denver Nuggets",
                                "price": 1.24
                            },
                            {
                                "name": "Portland Trail Blazers",
                                "price": 4.45
                            }
                        ]
                    },
                    {
                        "key": "spreads",
                        "last_update": "2024-02-23T13:40:35Z",
                        "outcomes": [
                            {
                                "name": "Denver Nuggets",
                                "price": 1.91,
                                "point": -9.5
                            },
                            {
                                "name": "Portland Trail Blazers",
                                "price": 1.91,
                                "point": 9.5
                            }
                        ]
                    },
                    {
                        "key": "totals",
                        "last_update": "2024-02-23T13:40:35Z",
                        "outcomes": [
                            {
                                "name": "Over",
                                "price": 1.91,
                                "point": 218.5
                            },
                            {
                                "name": "Under",
                                "price": 1.91,
                                "point": 218.5
                            }
                        ]
                    }
                ]
            },
            {
                "key": "williamhill_us",
                "title": "Caesars",
                "last_update": "2024-02-23T13:38:20Z",
                "markets": [
                    {
                        "key": "h2h",
                        "last_update": "2024-02-23T13:38:20Z",
                        "outcomes": [
                            {
                                "name": "Denver Nuggets",
                                "price": 1.22
                            },
                            {
                                "name": "Portland Trail Blazers",
                                "price": 4.45
                            }
                        ]
                    },
                    {
                        "key": "spreads",
                        "last_update": "2024-02-23T13:38:20Z",
                        "outcomes": [
                            {
                                "name": "Denver Nuggets",
                                "price": 1.91,
                                "point": -9.5
                            },
                            {
                                "name": "Portland Trail Blazers",
                                "price": 1.91,
                                "point": 9.5
                            }
                        ]
                    },
                    {
                        "key": "totals",
                        "last_update": "2024-02-23T13:38:20Z",
                        "outcomes": [
                            {
                                "name": "Over",
                                "price": 1.87,
                                "point": 218.5
                            },
                            {
                                "name": "Under",
                                "price": 1.95,
                                "point": 218.5
                            }
                        ]
                    }
                ]
            },
            {
                "key": "lowvig",
                "title": "LowVig.ag",
                "last_update": "2024-02-23T13:41:04Z",
                "markets": [
                    {
                        "key": "h2h",
                        "last_update": "2024-02-23T13:41:04Z",
                        "outcomes": [
                            {
                                "name": "Denver Nuggets",
                                "price": 1.24
                            },
                            {
                                "name": "Portland Trail Blazers",
                                "price": 4.45
                            }
                        ]
                    },
                    {
                        "key": "spreads",
                        "last_update": "2024-02-23T13:41:04Z",
                        "outcomes": [
                            {
                                "name": "Denver Nuggets",
                                "price": 1.94,
                                "point": -9.5
                            },
                            {
                                "name": "Portland Trail Blazers",
                                "price": 1.94,
                                "point": 9.5
                            }
                        ]
                    },
                    {
                        "key": "totals",
                        "last_update": "2024-02-23T13:41:04Z",
                        "outcomes": [
                            {
                                "name": "Over",
                                "price": 1.94,
                                "point": 218.5
                            },
                            {
                                "name": "Under",
                                "price": 1.94,
                                "point": 218.5
                            }
                        ]
                    }
                ]
            },
            {
                "key": "mybookieag",
                "title": "MyBookie.ag",
                "last_update": "2024-02-23T13:40:35Z",
                "markets": [
                    {
                        "key": "h2h",
                        "last_update": "2024-02-23T13:40:35Z",
                        "outcomes": [
                            {
                                "name": "Denver Nuggets",
                                "price": 1.22
                            },
                            {
                                "name": "Portland Trail Blazers",
                                "price": 4.25
                            }
                        ]
                    },
                    {
                        "key": "spreads",
                        "last_update": "2024-02-23T13:40:35Z",
                        "outcomes": [
                            {
                                "name": "Denver Nuggets",
                                "price": 1.91,
                                "point": -9.5
                            },
                            {
                                "name": "Portland Trail Blazers",
                                "price": 1.91,
                                "point": 9.5
                            }
                        ]
                    },
                    {
                        "key": "totals",
                        "last_update": "2024-02-23T13:40:35Z",
                        "outcomes": [
                            {
                                "name": "Over",
                                "price": 1.91,
                                "point": 218.0
                            },
                            {
                                "name": "Under",
                                "price": 1.91,
                                "point": 218.0
                            }
                        ]
                    }
                ]
            },
            {
                "key": "fanduel",
                "title": "FanDuel",
                "last_update": "2024-02-23T13:40:06Z",
                "markets": [
                    {
                        "key": "h2h",
                        "last_update": "2024-02-23T13:40:06Z",
                        "outcomes": [
                            {
                                "name": "Denver Nuggets",
                                "price": 1.22
                            },
                            {
                                "name": "Portland Trail Blazers",
                                "price": 4.6
                            }
                        ]
                    },
                    {
                        "key": "spreads",
                        "last_update": "2024-02-23T13:40:06Z",
                        "outcomes": [
                            {
                                "name": "Denver Nuggets",
                                "price": 1.88,
                                "point": -9.0
                            },
                            {
                                "name": "Portland Trail Blazers",
                                "price": 1.94,
                                "point": 9.0
                            }
                        ]
                    },
                    {
                        "key": "totals",
                        "last_update": "2024-02-23T13:40:06Z",
                        "outcomes": [
                            {
                                "name": "Over",
                                "price": 1.89,
                                "point": 218.0
                            },
                            {
                                "name": "Under",
                                "price": 1.93,
                                "point": 218.0
                            }
                        ]
                    }
                ]
            },
            {
                "key": "pointsbetus",
                "title": "PointsBet (US)",
                "last_update": "2024-02-23T13:40:35Z",
                "markets": [
                    {
                        "key": "h2h",
                        "last_update": "2024-02-23T13:40:35Z",
                        "outcomes": [
                            {
                                "name": "Denver Nuggets",
                                "price": 1.22
                            },
                            {
                                "name": "Portland Trail Blazers",
                                "price": 4.5
                            }
                        ]
                    },
                    {
                        "key": "spreads",
                        "last_update": "2024-02-23T13:40:35Z",
                        "outcomes": [
                            {
                                "name": "Denver Nuggets",
                                "price": 1.91,
                                "point": -9.5
                            },
                            {
                                "name": "Portland Trail Blazers",
                                "price": 1.91,
                                "point": 9.5
                            }
                        ]
                    },
                    {
                        "key": "totals",
                        "last_update": "2024-02-23T13:40:35Z",
                        "outcomes": [
                            {
                                "name": "Over",
                                "price": 1.91,
                                "point": 218.0
                            },
                            {
                                "name": "Under",
                                "price": 1.91,
                                "point": 218.0
                            }
                        ]
                    }
                ]
            },
            {
                "key": "bovada",
                "title": "Bovada",
                "last_update": "2024-02-23T13:41:03Z",
                "markets": [
                    {
                        "key": "h2h",
                        "last_update": "2024-02-23T13:41:03Z",
                        "outcomes": [
                            {
                                "name": "Denver Nuggets",
                                "price": 1.23
                            },
                            {
                                "name": "Portland Trail Blazers",
                                "price": 4.3
                            }
                        ]
                    },
                    {
                        "key": "spreads",
                        "last_update": "2024-02-23T13:41:03Z",
                        "outcomes": [
                            {
                                "name": "Denver Nuggets",
                                "price": 1.91,
                                "point": -9.5
                            },
                            {
                                "name": "Portland Trail Blazers",
                                "price": 1.91,
                                "point": 9.5
                            }
                        ]
                    },
                    {
                        "key": "totals",
                        "last_update": "2024-02-23T13:41:03Z",
                        "outcomes": [
                            {
                                "name": "Over",
                                "price": 1.91,
                                "point": 218.5
                            },
                            {
                                "name": "Under",
                                "price": 1.91,
                                "point": 218.5
                            }
                        ]
                    }
                ]
            },
            {
                "key": "betmgm",
                "title": "BetMGM",
                "last_update": "2024-02-23T13:38:20Z",
                "markets": [
                    {
                        "key": "h2h",
                        "last_update": "2024-02-23T13:38:20Z",
                        "outcomes": [
                            {
                                "name": "Denver Nuggets",
                                "price": 1.22
                            },
                            {
                                "name": "Portland Trail Blazers",
                                "price": 4.4
                            }
                        ]
                    },
                    {
                        "key": "spreads",
                        "last_update": "2024-02-23T13:38:20Z",
                        "outcomes": [
                            {
                                "name": "Denver Nuggets",
                                "price": 1.91,
                                "point": -9.5
                            },
                            {
                                "name": "Portland Trail Blazers",
                                "price": 1.91,
                                "point": 9.5
                            }
                        ]
                    },
                    {
                        "key": "totals",
                        "last_update": "2024-02-23T13:38:20Z",
                        "outcomes": [
                            {
                                "name": "Over",
                                "price": 1.91,
                                "point": 218.5
                            },
                            {
                                "name": "Under",
                                "price": 1.91,
                                "point": 218.5
                            }
                        ]
                    }
                ]
            },
            {
                "key": "betrivers",
                "title": "BetRivers",
                "last_update": "2024-02-23T13:40:36Z",
                "markets": [
                    {
                        "key": "h2h",
                        "last_update": "2024-02-23T13:40:36Z",
                        "outcomes": [
                            {
                                "name": "Denver Nuggets",
                                "price": 1.24
                            },
                            {
                                "name": "Portland Trail Blazers",
                                "price": 4.3
                            }
                        ]
                    },
                    {
                        "key": "spreads",
                        "last_update": "2024-02-23T13:40:36Z",
                        "outcomes": [
                            {
                                "name": "Denver Nuggets",
                                "price": 1.92,
                                "point": -9.5
                            },
                            {
                                "name": "Portland Trail Blazers",
                                "price": 1.89,
                                "point": 9.5
                            }
                        ]
                    },
                    {
                        "key": "totals",
                        "last_update": "2024-02-23T13:40:36Z",
                        "outcomes": [
                            {
                                "name": "Over",
                                "price": 1.89,
                                "point": 218.5
                            },
                            {
                                "name": "Under",
                                "price": 1.92,
                                "point": 218.5
                            }
                        ]
                    }
                ]
            },
            {
                "key": "unibet_us",
                "title": "Unibet",
                "last_update": "2024-02-23T13:40:36Z",
                "markets": [
                    {
                        "key": "h2h",
                        "last_update": "2024-02-23T13:40:36Z",
                        "outcomes": [
                            {
                                "name": "Denver Nuggets",
                                "price": 1.24
                            },
                            {
                                "name": "Portland Trail Blazers",
                                "price": 4.3
                            }
                        ]
                    },
                    {
                        "key": "spreads",
                        "last_update": "2024-02-23T13:40:36Z",
                        "outcomes": [
                            {
                                "name": "Denver Nuggets",
                                "price": 1.92,
                                "point": -9.5
                            },
                            {
                                "name": "Portland Trail Blazers",
                                "price": 1.89,
                                "point": 9.5
                            }
                        ]
                    },
                    {
                        "key": "totals",
                        "last_update": "2024-02-23T13:40:36Z",
                        "outcomes": [
                            {
                                "name": "Over",
                                "price": 1.89,
                                "point": 218.5
                            },
                            {
                                "name": "Under",
                                "price": 1.92,
                                "point": 218.5
                            }
                        ]
                    }
                ]
            },
            {
                "key": "wynnbet",
                "title": "WynnBET",
                "last_update": "2024-02-23T13:41:03Z",
                "markets": [
                    {
                        "key": "h2h",
                        "last_update": "2024-02-23T13:41:03Z",
                        "outcomes": [
                            {
                                "name": "Denver Nuggets",
                                "price": 1.23
                            },
                            {
                                "name": "Portland Trail Blazers",
                                "price": 4.5
                            }
                        ]
                    },
                    {
                        "key": "spreads",
                        "last_update": "2024-02-23T13:41:03Z",
                        "outcomes": [
                            {
                                "name": "Denver Nuggets",
                                "price": 1.91,
                                "point": -9.5
                            },
                            {
                                "name": "Portland Trail Blazers",
                                "price": 1.91,
                                "point": 9.5
                            }
                        ]
                    },
                    {
                        "key": "totals",
                        "last_update": "2024-02-23T13:41:03Z",
                        "outcomes": [
                            {
                                "name": "Over",
                                "price": 1.91,
                                "point": 218.0
                            },
                            {
                                "name": "Under",
                                "price": 1.91,
                                "point": 218.0
                            }
                        ]
                    }
                ]
            },
            {
                "key": "betus",
                "title": "BetUS",
                "last_update": "2024-02-23T13:40:36Z",
                "markets": [
                    {
                        "key": "h2h",
                        "last_update": "2024-02-23T13:40:36Z",
                        "outcomes": [
                            {
                                "name": "Denver Nuggets",
                                "price": 1.23
                            },
                            {
                                "name": "Portland Trail Blazers",
                                "price": 4.38
                            }
                        ]
                    },
                    {
                        "key": "spreads",
                        "last_update": "2024-02-23T13:40:36Z",
                        "outcomes": [
                            {
                                "name": "Denver Nuggets",
                                "price": 1.91,
                                "point": -9.5
                            },
                            {
                                "name": "Portland Trail Blazers",
                                "price": 1.91,
                                "point": 9.5
                            }
                        ]
                    },
                    {
                        "key": "totals",
                        "last_update": "2024-02-23T13:40:36Z",
                        "outcomes": [
                            {
                                "name": "Over",
                                "price": 1.91,
                                "point": 219.0
                            },
                            {
                                "name": "Under",
                                "price": 1.91,
                                "point": 219.0
                            }
                        ]
                    }
                ]
            }
        ]
    },
    {
        "id": "87b4d03c3dbdd99d2dad6c8ef097247f",
        "sport_key": "basketball_nba",
        "sport_title": "NBA",
        "commence_time": "2024-02-24T03:10:00Z",
        "home_team": "Minnesota Timberwolves",
        "away_team": "Milwaukee Bucks",
        "bookmakers": [
            {
                "key": "draftkings",
                "title": "DraftKings",
                "last_update": "2024-02-23T13:40:35Z",
                "markets": [
                    {
                        "key": "h2h",
                        "last_update": "2024-02-23T13:40:35Z",
                        "outcomes": [
                            {
                                "name": "Milwaukee Bucks",
                                "price": 2.45
                            },
                            {
                                "name": "Minnesota Timberwolves",
                                "price": 1.57
                            }
                        ]
                    },
                    {
                        "key": "spreads",
                        "last_update": "2024-02-23T13:40:35Z",
                        "outcomes": [
                            {
                                "name": "Milwaukee Bucks",
                                "price": 1.91,
                                "point": 4.0
                            },
                            {
                                "name": "Minnesota Timberwolves",
                                "price": 1.91,
                                "point": -4.0
                            }
                        ]
                    },
                    {
                        "key": "totals",
                        "last_update": "2024-02-23T13:40:35Z",
                        "outcomes": [
                            {
                                "name": "Over",
                                "price": 1.93,
                                "point": 225.0
                            },
                            {
                                "name": "Under",
                                "price": 1.89,
                                "point": 225.0
                            }
                        ]
                    }
                ]
            },
            {
                "key": "lowvig",
                "title": "LowVig.ag",
                "last_update": "2024-02-23T13:41:04Z",
                "markets": [
                    {
                        "key": "h2h",
                        "last_update": "2024-02-23T13:41:04Z",
                        "outcomes": [
                            {
                                "name": "Milwaukee Bucks",
                                "price": 2.5
                            },
                            {
                                "name": "Minnesota Timberwolves",
                                "price": 1.59
                            }
                        ]
                    },
                    {
                        "key": "spreads",
                        "last_update": "2024-02-23T13:41:04Z",
                        "outcomes": [
                            {
                                "name": "Milwaukee Bucks",
                                "price": 1.93,
                                "point": 4.0
                            },
                            {
                                "name": "Minnesota Timberwolves",
                                "price": 1.96,
                                "point": -4.0
                            }
                        ]
                    },
                    {
                        "key": "totals",
                        "last_update": "2024-02-23T13:41:04Z",
                        "outcomes": [
                            {
                                "name": "Over",
                                "price": 1.94,
                                "point": 225.0
                            },
                            {
                                "name": "Under",
                                "price": 1.94,
                                "point": 225.0
                            }
                        ]
                    }
                ]
            },
            {
                "key": "betonlineag",
                "title": "BetOnline.ag",
                "last_update": "2024-02-23T13:40:35Z",
                "markets": [
                    {
                        "key": "h2h",
                        "last_update": "2024-02-23T13:40:35Z",
                        "outcomes": [
                            {
                                "name": "Milwaukee Bucks",
                                "price": 2.5
                            },
                            {
                                "name": "Minnesota Timberwolves",
                                "price": 1.59
                            }
                        ]
                    },
                    {
                        "key": "spreads",
                        "last_update": "2024-02-23T13:40:35Z",
                        "outcomes": [
                            {
                                "name": "Milwaukee Bucks",
                                "price": 1.89,
                                "point": 4.0
                            },
                            {
                                "name": "Minnesota Timberwolves",
                                "price": 1.93,
                                "point": -4.0
                            }
                        ]
                    },
                    {
                        "key": "totals",
                        "last_update": "2024-02-23T13:40:35Z",
                        "outcomes": [
                            {
                                "name": "Over",
                                "price": 1.91,
                                "point": 225.0
                            },
                            {
                                "name": "Under",
                                "price": 1.91,
                                "point": 225.0
                            }
                        ]
                    }
                ]
            },
            {
                "key": "williamhill_us",
                "title": "Caesars",
                "last_update": "2024-02-23T13:38:20Z",
                "markets": [
                    {
                        "key": "h2h",
                        "last_update": "2024-02-23T13:38:20Z",
                        "outcomes": [
                            {
                                "name": "Milwaukee Bucks",
                                "price": 2.43
                            },
                            {
                                "name": "Minnesota Timberwolves",
                                "price": 1.59
                            }
                        ]
                    },
                    {
                        "key": "spreads",
                        "last_update": "2024-02-23T13:38:20Z",
                        "outcomes": [
                            {
                                "name": "Milwaukee Bucks",
                                "price": 1.91,
                                "point": 4.0
                            },
                            {
                                "name": "Minnesota Timberwolves",
                                "price": 1.91,
                                "point": -4.0
                            }
                        ]
                    },
                    {
                        "key": "totals",
                        "last_update": "2024-02-23T13:38:20Z",
                        "outcomes": [
                            {
                                "name": "Over",
                                "price": 1.91,
                                "point": 225.0
                            },
                            {
                                "name": "Under",
                                "price": 1.91,
                                "point": 225.0
                            }
                        ]
                    }
                ]
            },
            {
                "key": "wynnbet",
                "title": "WynnBET",
                "last_update": "2024-02-23T13:41:03Z",
                "markets": [
                    {
                        "key": "h2h",
                        "last_update": "2024-02-23T13:41:03Z",
                        "outcomes": [
                            {
                                "name": "Milwaukee Bucks",
                                "price": 2.43
                            },
                            {
                                "name": "Minnesota Timberwolves",
                                "price": 1.59
                            }
                        ]
                    },
                    {
                        "key": "spreads",
                        "last_update": "2024-02-23T13:41:03Z",
                        "outcomes": [
                            {
                                "name": "Milwaukee Bucks",
                                "price": 1.91,
                                "point": 4.0
                            },
                            {
                                "name": "Minnesota Timberwolves",
                                "price": 1.91,
                                "point": -4.0
                            }
                        ]
                    },
                    {
                        "key": "totals",
                        "last_update": "2024-02-23T13:41:03Z",
                        "outcomes": [
                            {
                                "name": "Over",
                                "price": 1.91,
                                "point": 225.5
                            },
                            {
                                "name": "Under",
                                "price": 1.91,
                                "point": 225.5
                            }
                        ]
                    }
                ]
            },
            {
                "key": "mybookieag",
                "title": "MyBookie.ag",
                "last_update": "2024-02-23T13:40:35Z",
                "markets": [
                    {
                        "key": "h2h",
                        "last_update": "2024-02-23T13:40:35Z",
                        "outcomes": [
                            {
                                "name": "Milwaukee Bucks",
                                "price": 2.45
                            },
                            {
                                "name": "Minnesota Timberwolves",
                                "price": 1.59
                            }
                        ]
                    },
                    {
                        "key": "spreads",
                        "last_update": "2024-02-23T13:40:35Z",
                        "outcomes": [
                            {
                                "name": "Milwaukee Bucks",
                                "price": 1.91,
                                "point": 4.0
                            },
                            {
                                "name": "Minnesota Timberwolves",
                                "price": 1.91,
                                "point": -4.0
                            }
                        ]
                    },
                    {
                        "key": "totals",
                        "last_update": "2024-02-23T13:40:35Z",
                        "outcomes": [
                            {
                                "name": "Over",
                                "price": 1.91,
                                "point": 225.0
                            },
                            {
                                "name": "Under",
                                "price": 1.91,
                                "point": 225.0
                            }
                        ]
                    }
                ]
            },
            {
                "key": "fanduel",
                "title": "FanDuel",
                "last_update": "2024-02-23T13:40:06Z",
                "markets": [
                    {
                        "key": "h2h",
                        "last_update": "2024-02-23T13:40:06Z",
                        "outcomes": [
                            {
                                "name": "Milwaukee Bucks",
                                "price": 2.42
                            },
                            {
                                "name": "Minnesota Timberwolves",
                                "price": 1.6
                            }
                        ]
                    },
                    {
                        "key": "spreads",
                        "last_update": "2024-02-23T13:40:06Z",
                        "outcomes": [
                            {
                                "name": "Milwaukee Bucks",
                                "price": 1.91,
                                "point": 4.0
                            },
                            {
                                "name": "Minnesota Timberwolves",
                                "price": 1.91,
                                "point": -4.0
                            }
                        ]
                    },
                    {
                        "key": "totals",
                        "last_update": "2024-02-23T13:40:06Z",
                        "outcomes": [
                            {
                                "name": "Over",
                                "price": 1.91,
                                "point": 225.0
                            },
                            {
                                "name": "Under",
                                "price": 1.91,
                                "point": 225.0
                            }
                        ]
                    }
                ]
            },
            {
                "key": "pointsbetus",
                "title": "PointsBet (US)",
                "last_update": "2024-02-23T13:40:35Z",
                "markets": [
                    {
                        "key": "h2h",
                        "last_update": "2024-02-23T13:40:35Z",
                        "outcomes": [
                            {
                                "name": "Milwaukee Bucks",
                                "price": 2.5
                            },
                            {
                                "name": "Minnesota Timberwolves",
                                "price": 1.56
                            }
                        ]
                    },
                    {
                        "key": "spreads",
                        "last_update": "2024-02-23T13:40:35Z",
                        "outcomes": [
                            {
                                "name": "Milwaukee Bucks",
                                "price": 1.91,
                                "point": 4.0
                            },
                            {
                                "name": "Minnesota Timberwolves",
                                "price": 1.91,
                                "point": -4.0
                            }
                        ]
                    },
                    {
                        "key": "totals",
                        "last_update": "2024-02-23T13:40:35Z",
                        "outcomes": [
                            {
                                "name": "Over",
                                "price": 1.91,
                                "point": 224.5
                            },
                            {
                                "name": "Under",
                                "price": 1.91,
                                "point": 224.5
                            }
                        ]
                    }
                ]
            },
            {
                "key": "bovada",
                "title": "Bovada",
                "last_update": "2024-02-23T13:41:03Z",
                "markets": [
                    {
                        "key": "h2h",
                        "last_update": "2024-02-23T13:41:03Z",
                        "outcomes": [
                            {
                                "name": "Milwaukee Bucks",
                                "price": 2.45
                            },
                            {
                                "name": "Minnesota Timberwolves",
                                "price": 1.59
                            }
                        ]
                    },
                    {
                        "key": "spreads",
                        "last_update": "2024-02-23T13:41:03Z",
                        "outcomes": [
                            {
                                "name": "Milwaukee Bucks",
                                "price": 1.91,
                                "point": 4.0
                            },
                            {
                                "name": "Minnesota Timberwolves",
                                "price": 1.91,
                                "point": -4.0
                            }
                        ]
                    },
                    {
                        "key": "totals",
                        "last_update": "2024-02-23T13:41:03Z",
                        "outcomes": [
                            {
                                "name": "Over",
                                "price": 1.91,
                                "point": 225.5
                            },
                            {
                                "name": "Under",
                                "price": 1.91,
                                "point": 225.5
                            }
                        ]
                    }
                ]
            },
            {
                "key": "superbook",
                "title": "SuperBook",
                "last_update": "2024-02-23T13:40:36Z",
                "markets": [
                    {
                        "key": "h2h",
                        "last_update": "2024-02-23T13:40:36Z",
                        "outcomes": [
                            {
                                "name": "Milwaukee Bucks",
                                "price": 2.5
                            },
                            {
                                "name": "Minnesota Timberwolves",
                                "price": 1.59
                            }
                        ]
                    },
                    {
                        "key": "spreads",
                        "last_update": "2024-02-23T13:40:36Z",
                        "outcomes": [
                            {
                                "name": "Milwaukee Bucks",
                                "price": 1.91,
                                "point": 4.0
                            },
                            {
                                "name": "Minnesota Timberwolves",
                                "price": 1.91,
                                "point": -4.0
                            }
                        ]
                    },
                    {
                        "key": "totals",
                        "last_update": "2024-02-23T13:40:36Z",
                        "outcomes": [
                            {
                                "name": "Over",
                                "price": 1.91,
                                "point": 225.5
                            },
                            {
                                "name": "Under",
                                "price": 1.91,
                                "point": 225.5
                            }
                        ]
                    }
                ]
            },
            {
                "key": "betmgm",
                "title": "BetMGM",
                "last_update": "2024-02-23T13:38:20Z",
                "markets": [
                    {
                        "key": "h2h",
                        "last_update": "2024-02-23T13:38:20Z",
                        "outcomes": [
                            {
                                "name": "Milwaukee Bucks",
                                "price": 2.45
                            },
                            {
                                "name": "Minnesota Timberwolves",
                                "price": 1.57
                            }
                        ]
                    },
                    {
                        "key": "spreads",
                        "last_update": "2024-02-23T13:38:20Z",
                        "outcomes": [
                            {
                                "name": "Milwaukee Bucks",
                                "price": 1.95,
                                "point": 3.5
                            },
                            {
                                "name": "Minnesota Timberwolves",
                                "price": 1.87,
                                "point": -3.5
                            }
                        ]
                    },
                    {
                        "key": "totals",
                        "last_update": "2024-02-23T13:38:20Z",
                        "outcomes": [
                            {
                                "name": "Over",
                                "price": 1.91,
                                "point": 225.5
                            },
                            {
                                "name": "Under",
                                "price": 1.91,
                                "point": 225.5
                            }
                        ]
                    }
                ]
            },
            {
                "key": "unibet_us",
                "title": "Unibet",
                "last_update": "2024-02-23T13:40:36Z",
                "markets": [
                    {
                        "key": "h2h",
                        "last_update": "2024-02-23T13:40:36Z",
                        "outcomes": [
                            {
                                "name": "Milwaukee Bucks",
                                "price": 2.48
                            },
                            {
                                "name": "Minnesota Timberwolves",
                                "price": 1.56
                            }
                        ]
                    },
                    {
                        "key": "spreads",
                        "last_update": "2024-02-23T13:40:36Z",
                        "outcomes": [
                            {
                                "name": "Milwaukee Bucks",
                                "price": 1.92,
                                "point": 4.0
                            },
                            {
                                "name": "Minnesota Timberwolves",
                                "price": 1.89,
                                "point": -4.0
                            }
                        ]
                    },
                    {
                        "key": "totals",
                        "last_update": "2024-02-23T13:40:36Z",
                        "outcomes": [
                            {
                                "name": "Over",
                                "price": 1.92,
                                "point": 225.5
                            },
                            {
                                "name": "Under",
                                "price": 1.89,
                                "point": 225.5
                            }
                        ]
                    }
                ]
            },
            {
                "key": "betrivers",
                "title": "BetRivers",
                "last_update": "2024-02-23T13:40:36Z",
                "markets": [
                    {
                        "key": "h2h",
                        "last_update": "2024-02-23T13:40:36Z",
                        "outcomes": [
                            {
                                "name": "Milwaukee Bucks",
                                "price": 2.48
                            },
                            {
                                "name": "Minnesota Timberwolves",
                                "price": 1.56
                            }
                        ]
                    },
                    {
                        "key": "spreads",
                        "last_update": "2024-02-23T13:40:36Z",
                        "outcomes": [
                            {
                                "name": "Milwaukee Bucks",
                                "price": 1.92,
                                "point": 4.0
                            },
                            {
                                "name": "Minnesota Timberwolves",
                                "price": 1.89,
                                "point": -4.0
                            }
                        ]
                    },
                    {
                        "key": "totals",
                        "last_update": "2024-02-23T13:40:36Z",
                        "outcomes": [
                            {
                                "name": "Over",
                                "price": 1.92,
                                "point": 225.5
                            },
                            {
                                "name": "Under",
                                "price": 1.89,
                                "point": 225.5
                            }
                        ]
                    }
                ]
            },
            {
                "key": "betus",
                "title": "BetUS",
                "last_update": "2024-02-23T13:40:36Z",
                "markets": [
                    {
                        "key": "h2h",
                        "last_update": "2024-02-23T13:40:36Z",
                        "outcomes": [
                            {
                                "name": "Milwaukee Bucks",
                                "price": 2.48
                            },
                            {
                                "name": "Minnesota Timberwolves",
                                "price": 1.59
                            }
                        ]
                    },
                    {
                        "key": "spreads",
                        "last_update": "2024-02-23T13:40:36Z",
                        "outcomes": [
                            {
                                "name": "Milwaukee Bucks",
                                "price": 1.91,
                                "point": 4.0
                            },
                            {
                                "name": "Minnesota Timberwolves",
                                "price": 1.91,
                                "point": -4.0
                            }
                        ]
                    },
                    {
                        "key": "totals",
                        "last_update": "2024-02-23T13:40:36Z",
                        "outcomes": [
                            {
                                "name": "Over",
                                "price": 1.91,
                                "point": 225.5
                            },
                            {
                                "name": "Under",
                                "price": 1.91,
                                "point": 225.5
                            }
                        ]
                    }
                ]
            }
        ]
    },
    {
        "id": "3b42391ffda56180c1c35a2b9d327fa4",
        "sport_key": "basketball_nba",
        "sport_title": "NBA",
        "commence_time": "2024-02-24T03:40:00Z",
        "home_team": "Los Angeles Lakers",
        "away_team": "San Antonio Spurs",
        "bookmakers": [
            {
                "key": "draftkings",
                "title": "DraftKings",
                "last_update": "2024-02-23T13:40:35Z",
                "markets": [
                    {
                        "key": "h2h",
                        "last_update": "2024-02-23T13:40:35Z",
                        "outcomes": [
                            {
                                "name": "Los Angeles Lakers",
                                "price": 1.23
                            },
                            {
                                "name": "San Antonio Spurs",
                                "price": 4.4
                            }
                        ]
                    },
                    {
                        "key": "spreads",
                        "last_update": "2024-02-23T13:40:35Z",
                        "outcomes": [
                            {
                                "name": "Los Angeles Lakers",
                                "price": 1.89,
                                "point": -10.0
                            },
                            {
                                "name": "San Antonio Spurs",
                                "price": 1.93,
                                "point": 10.0
                            }
                        ]
                    },
                    {
                        "key": "totals",
                        "last_update": "2024-02-23T13:40:35Z",
                        "outcomes": [
                            {
                                "name": "Over",
                                "price": 1.91,
                                "point": 239.5
                            },
                            {
                                "name": "Under",
                                "price": 1.91,
                                "point": 239.5
                            }
                        ]
                    }
                ]
            },
            {
                "key": "pointsbetus",
                "title": "PointsBet (US)",
                "last_update": "2024-02-23T13:40:35Z",
                "markets": [
                    {
                        "key": "h2h",
                        "last_update": "2024-02-23T13:40:35Z",
                        "outcomes": [
                            {
                                "name": "Los Angeles Lakers",
                                "price": 1.22
                            },
                            {
                                "name": "San Antonio Spurs",
                                "price": 4.5
                            }
                        ]
                    },
                    {
                        "key": "spreads",
                        "last_update": "2024-02-23T13:40:35Z",
                        "outcomes": [
                            {
                                "name": "Los Angeles Lakers",
                                "price": 1.91,
                                "point": -10.0
                            },
                            {
                                "name": "San Antonio Spurs",
                                "price": 1.91,
                                "point": 10.0
                            }
                        ]
                    },
                    {
                        "key": "totals",
                        "last_update": "2024-02-23T13:40:35Z",
                        "outcomes": [
                            {
                                "name": "Over",
                                "price": 1.91,
                                "point": 239.5
                            },
                            {
                                "name": "Under",
                                "price": 1.91,
                                "point": 239.5
                            }
                        ]
                    }
                ]
            },
            {
                "key": "mybookieag",
                "title": "MyBookie.ag",
                "last_update": "2024-02-23T13:40:35Z",
                "markets": [
                    {
                        "key": "h2h",
                        "last_update": "2024-02-23T13:40:35Z",
                        "outcomes": [
                            {
                                "name": "Los Angeles Lakers",
                                "price": 1.22
                            },
                            {
                                "name": "San Antonio Spurs",
                                "price": 4.25
                            }
                        ]
                    },
                    {
                        "key": "spreads",
                        "last_update": "2024-02-23T13:40:35Z",
                        "outcomes": [
                            {
                                "name": "Los Angeles Lakers",
                                "price": 1.91,
                                "point": -9.5
                            },
                            {
                                "name": "San Antonio Spurs",
                                "price": 1.91,
                                "point": 9.5
                            }
                        ]
                    },
                    {
                        "key": "totals",
                        "last_update": "2024-02-23T13:40:35Z",
                        "outcomes": [
                            {
                                "name": "Over",
                                "price": 1.91,
                                "point": 239.5
                            },
                            {
                                "name": "Under",
                                "price": 1.91,
                                "point": 239.5
                            }
                        ]
                    }
                ]
            },
            {
                "key": "wynnbet",
                "title": "WynnBET",
                "last_update": "2024-02-23T13:41:03Z",
                "markets": [
                    {
                        "key": "h2h",
                        "last_update": "2024-02-23T13:41:03Z",
                        "outcomes": [
                            {
                                "name": "Los Angeles Lakers",
                                "price": 1.23
                            },
                            {
                                "name": "San Antonio Spurs",
                                "price": 4.5
                            }
                        ]
                    },
                    {
                        "key": "spreads",
                        "last_update": "2024-02-23T13:41:03Z",
                        "outcomes": [
                            {
                                "name": "Los Angeles Lakers",
                                "price": 1.91,
                                "point": -10.0
                            },
                            {
                                "name": "San Antonio Spurs",
                                "price": 1.91,
                                "point": 10.0
                            }
                        ]
                    },
                    {
                        "key": "totals",
                        "last_update": "2024-02-23T13:41:03Z",
                        "outcomes": [
                            {
                                "name": "Over",
                                "price": 1.91,
                                "point": 239.5
                            },
                            {
                                "name": "Under",
                                "price": 1.91,
                                "point": 239.5
                            }
                        ]
                    }
                ]
            },
            {
                "key": "fanduel",
                "title": "FanDuel",
                "last_update": "2024-02-23T13:40:06Z",
                "markets": [
                    {
                        "key": "h2h",
                        "last_update": "2024-02-23T13:40:06Z",
                        "outcomes": [
                            {
                                "name": "Los Angeles Lakers",
                                "price": 1.22
                            },
                            {
                                "name": "San Antonio Spurs",
                                "price": 4.6
                            }
                        ]
                    },
                    {
                        "key": "spreads",
                        "last_update": "2024-02-23T13:40:06Z",
                        "outcomes": [
                            {
                                "name": "Los Angeles Lakers",
                                "price": 1.91,
                                "point": -10.0
                            },
                            {
                                "name": "San Antonio Spurs",
                                "price": 1.91,
                                "point": 10.0
                            }
                        ]
                    },
                    {
                        "key": "totals",
                        "last_update": "2024-02-23T13:40:06Z",
                        "outcomes": [
                            {
                                "name": "Over",
                                "price": 1.91,
                                "point": 239.5
                            },
                            {
                                "name": "Under",
                                "price": 1.91,
                                "point": 239.5
                            }
                        ]
                    }
                ]
            },
            {
                "key": "betmgm",
                "title": "BetMGM",
                "last_update": "2024-02-23T13:38:20Z",
                "markets": [
                    {
                        "key": "h2h",
                        "last_update": "2024-02-23T13:38:20Z",
                        "outcomes": [
                            {
                                "name": "Los Angeles Lakers",
                                "price": 1.22
                            },
                            {
                                "name": "San Antonio Spurs",
                                "price": 4.5
                            }
                        ]
                    },
                    {
                        "key": "spreads",
                        "last_update": "2024-02-23T13:38:20Z",
                        "outcomes": [
                            {
                                "name": "Los Angeles Lakers",
                                "price": 1.87,
                                "point": -9.5
                            },
                            {
                                "name": "San Antonio Spurs",
                                "price": 1.95,
                                "point": 9.5
                            }
                        ]
                    },
                    {
                        "key": "totals",
                        "last_update": "2024-02-23T13:38:20Z",
                        "outcomes": [
                            {
                                "name": "Over",
                                "price": 1.91,
                                "point": 239.5
                            },
                            {
                                "name": "Under",
                                "price": 1.91,
                                "point": 239.5
                            }
                        ]
                    }
                ]
            },
            {
                "key": "betrivers",
                "title": "BetRivers",
                "last_update": "2024-02-23T13:40:36Z",
                "markets": [
                    {
                        "key": "h2h",
                        "last_update": "2024-02-23T13:40:36Z",
                        "outcomes": [
                            {
                                "name": "Los Angeles Lakers",
                                "price": 1.22
                            },
                            {
                                "name": "San Antonio Spurs",
                                "price": 4.5
                            }
                        ]
                    },
                    {
                        "key": "spreads",
                        "last_update": "2024-02-23T13:40:36Z",
                        "outcomes": [
                            {
                                "name": "Los Angeles Lakers",
                                "price": 1.93,
                                "point": -10.0
                            },
                            {
                                "name": "San Antonio Spurs",
                                "price": 1.88,
                                "point": 10.0
                            }
                        ]
                    },
                    {
                        "key": "totals",
                        "last_update": "2024-02-23T13:40:36Z",
                        "outcomes": [
                            {
                                "name": "Over",
                                "price": 1.92,
                                "point": 239.0
                            },
                            {
                                "name": "Under",
                                "price": 1.89,
                                "point": 239.0
                            }
                        ]
                    }
                ]
            },
            {
                "key": "unibet_us",
                "title": "Unibet",
                "last_update": "2024-02-23T13:40:36Z",
                "markets": [
                    {
                        "key": "h2h",
                        "last_update": "2024-02-23T13:40:36Z",
                        "outcomes": [
                            {
                                "name": "Los Angeles Lakers",
                                "price": 1.22
                            },
                            {
                                "name": "San Antonio Spurs",
                                "price": 4.5
                            }
                        ]
                    },
                    {
                        "key": "spreads",
                        "last_update": "2024-02-23T13:40:36Z",
                        "outcomes": [
                            {
                                "name": "Los Angeles Lakers",
                                "price": 1.93,
                                "point": -10.0
                            },
                            {
                                "name": "San Antonio Spurs",
                                "price": 1.88,
                                "point": 10.0
                            }
                        ]
                    },
                    {
                        "key": "totals",
                        "last_update": "2024-02-23T13:40:36Z",
                        "outcomes": [
                            {
                                "name": "Over",
                                "price": 1.92,
                                "point": 239.0
                            },
                            {
                                "name": "Under",
                                "price": 1.89,
                                "point": 239.0
                            }
                        ]
                    }
                ]
            },
            {
                "key": "williamhill_us",
                "title": "Caesars",
                "last_update": "2024-02-23T13:38:20Z",
                "markets": [
                    {
                        "key": "h2h",
                        "last_update": "2024-02-23T13:38:20Z",
                        "outcomes": [
                            {
                                "name": "Los Angeles Lakers",
                                "price": 1.21
                            },
                            {
                                "name": "San Antonio Spurs",
                                "price": 4.6
                            }
                        ]
                    },
                    {
                        "key": "spreads",
                        "last_update": "2024-02-23T13:38:20Z",
                        "outcomes": [
                            {
                                "name": "Los Angeles Lakers",
                                "price": 1.91,
                                "point": -10.0
                            },
                            {
                                "name": "San Antonio Spurs",
                                "price": 1.91,
                                "point": 10.0
                            }
                        ]
                    },
                    {
                        "key": "totals",
                        "last_update": "2024-02-23T13:38:20Z",
                        "outcomes": [
                            {
                                "name": "Over",
                                "price": 1.91,
                                "point": 239.5
                            },
                            {
                                "name": "Under",
                                "price": 1.91,
                                "point": 239.5
                            }
                        ]
                    }
                ]
            },
            {
                "key": "bovada",
                "title": "Bovada",
                "last_update": "2024-02-23T13:41:03Z",
                "markets": [
                    {
                        "key": "h2h",
                        "last_update": "2024-02-23T13:41:03Z",
                        "outcomes": [
                            {
                                "name": "Los Angeles Lakers",
                                "price": 1.2
                            },
                            {
                                "name": "San Antonio Spurs",
                                "price": 4.6
                            }
                        ]
                    },
                    {
                        "key": "spreads",
                        "last_update": "2024-02-23T13:41:03Z",
                        "outcomes": [
                            {
                                "name": "Los Angeles Lakers",
                                "price": 1.91,
                                "point": -10.0
                            },
                            {
                                "name": "San Antonio Spurs",
                                "price": 1.91,
                                "point": 10.0
                            }
                        ]
                    },
                    {
                        "key": "totals",
                        "last_update": "2024-02-23T13:41:03Z",
                        "outcomes": [
                            {
                                "name": "Over",
                                "price": 1.91,
                                "point": 239.5
                            },
                            {
                                "name": "Under",
                                "price": 1.91,
                                "point": 239.5
                            }
                        ]
                    }
                ]
            },
            {
                "key": "lowvig",
                "title": "LowVig.ag",
                "last_update": "2024-02-23T13:41:04Z",
                "markets": [
                    {
                        "key": "h2h",
                        "last_update": "2024-02-23T13:41:04Z",
                        "outcomes": [
                            {
                                "name": "Los Angeles Lakers",
                                "price": 1.24
                            },
                            {
                                "name": "San Antonio Spurs",
                                "price": 4.45
                            }
                        ]
                    },
                    {
                        "key": "spreads",
                        "last_update": "2024-02-23T13:41:04Z",
                        "outcomes": [
                            {
                                "name": "Los Angeles Lakers",
                                "price": 1.94,
                                "point": -10.0
                            },
                            {
                                "name": "San Antonio Spurs",
                                "price": 1.94,
                                "point": 10.0
                            }
                        ]
                    },
                    {
                        "key": "totals",
                        "last_update": "2024-02-23T13:41:04Z",
                        "outcomes": [
                            {
                                "name": "Over",
                                "price": 1.94,
                                "point": 239.5
                            },
                            {
                                "name": "Under",
                                "price": 1.94,
                                "point": 239.5
                            }
                        ]
                    }
                ]
            },
            {
                "key": "betonlineag",
                "title": "BetOnline.ag",
                "last_update": "2024-02-23T13:40:35Z",
                "markets": [
                    {
                        "key": "h2h",
                        "last_update": "2024-02-23T13:40:35Z",
                        "outcomes": [
                            {
                                "name": "Los Angeles Lakers",
                                "price": 1.24
                            },
                            {
                                "name": "San Antonio Spurs",
                                "price": 4.45
                            }
                        ]
                    },
                    {
                        "key": "spreads",
                        "last_update": "2024-02-23T13:40:35Z",
                        "outcomes": [
                            {
                                "name": "Los Angeles Lakers",
                                "price": 1.91,
                                "point": -10.0
                            },
                            {
                                "name": "San Antonio Spurs",
                                "price": 1.91,
                                "point": 10.0
                            }
                        ]
                    },
                    {
                        "key": "totals",
                        "last_update": "2024-02-23T13:40:35Z",
                        "outcomes": [
                            {
                                "name": "Over",
                                "price": 1.91,
                                "point": 239.5
                            },
                            {
                                "name": "Under",
                                "price": 1.91,
                                "point": 239.5
                            }
                        ]
                    }
                ]
            },
            {
                "key": "betus",
                "title": "BetUS",
                "last_update": "2024-02-23T13:40:36Z",
                "markets": [
                    {
                        "key": "h2h",
                        "last_update": "2024-02-23T13:40:36Z",
                        "outcomes": [
                            {
                                "name": "Los Angeles Lakers",
                                "price": 1.2
                            },
                            {
                                "name": "San Antonio Spurs",
                                "price": 4.75
                            }
                        ]
                    },
                    {
                        "key": "spreads",
                        "last_update": "2024-02-23T13:40:36Z",
                        "outcomes": [
                            {
                                "name": "Los Angeles Lakers",
                                "price": 1.91,
                                "point": -10.0
                            },
                            {
                                "name": "San Antonio Spurs",
                                "price": 1.91,
                                "point": 10.0
                            }
                        ]
                    },
                    {
                        "key": "totals",
                        "last_update": "2024-02-23T13:40:36Z",
                        "outcomes": [
                            {
                                "name": "Over",
                                "price": 1.91,
                                "point": 239.0
                            },
                            {
                                "name": "Under",
                                "price": 1.91,
                                "point": 239.0
                            }
                        ]
                    }
                ]
            }
        ]
    }
]

@shared_task
def update_events_and_lines():
    from .models import Event, Line
    logger.info("update_events_and_lines task starting")
    res = _getObject()

    for event in res:
        key = event['id']
        sport_key = event['sport_key']
        sport_title = event['sport_title']
        start_time = event['commence_time']
        home_team = event['home_team']
        away_team = event['away_team']
        logger.info("update_events_and_lines event %s parsing" % id)
        eventObj, created = Event.objects.get_or_create(
            event_key = key,
            defaults = {
                'sport_key': sport_key,
                'sport_title': sport_title,
                'home_team': home_team,
                'away_team': away_team,
                'start_time': start_time
            }
        )
        
        #Go through each type of bet
        try:
            markets = event['bookmakers'][0]['markets']
        except:
            logger.info("No markets found for Event %s" % id)
        
        for market in markets:
            for outcome in market['outcomes']:
                line_type = market['key']
                name = outcome['name']
                price = outcome['price']
                point = outcome.get('point', None)
                updated = market['last_update']

                Line.objects.update_or_create(
                    event = eventObj,
                    line_type = line_type,
                    name = name,
                    defaults = {
                        'price': price,
                        'point': point,
                        'updated': updated
                    }
                )
        
    logger.info("update_events_and_lines task finished")
