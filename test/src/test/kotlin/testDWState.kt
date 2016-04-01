package DWSTester

import java.io.File
import kotlin.test.*
import org.junit.Test as test

import datawire_connect.state.DatawireState

class TestDWState {
	@test fun check() {
		val path: String = System.getProperty("GoldPath")

		println("running check " + path)

		val goldInfo = File(path).readLines()

		var i: Int = 0

		val goldDefaultPath = goldInfo[i++]
		val goldOrgID = goldInfo[i++]
		val goldEmail = goldInfo[i++]

		println("goldDefaultPath " + goldDefaultPath)

		val goldTokens: MutableMap<String, String> = hashMapOf()
		val services: MutableSet<String> = mutableSetOf()

		// Yeah, I know, this isn't terribly Kotlinesque. Cope. [ :) ]
		goldInfo.takeLast(goldInfo.size - i).forEach {
			val fields = it.split(":::")

			val svcHandle = fields[0]
			val svcToken = fields[1]

			goldTokens[svcHandle] = svcToken
			services.add(svcHandle)
		}

        var dwState = DatawireState();

		assertEquals(dwState.defaultStatePath(), goldDefaultPath);

        dwState = DatawireState.defaultState();

		assertEquals(dwState.getCurrentOrgID(), goldOrgID);
		assertEquals(dwState.getCurrentEmail(), goldEmail);

		val goodTokens: Set<String> = 
			services.fold(setOf(), 
				          { acc, it -> 
				          	if (goldTokens[it] == dwState.getCurrentServiceToken(it)) 
				          	    acc + it
				          	else
				          	    acc })

		val dwStateServices: Set<String> = dwState.getCurrentServices().toSet()

		assertEquals(goodTokens, services)
		assertEquals(goodTokens, dwStateServices)
	}
}
